import asyncio, logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import BOT_TOKEN, ADMIN_CHAT_ID
import keyboards as kb

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class BookingState(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_service = State()

SERVICES = {
    "1": {"name": "💆‍♀️ ინდივიდუალური სესია",    "price": "111€", "desc": "ჰოლისტიკური სესია — ფსიქო-სომატიკა, NLP, ჰიპნოთერაპია."},
    "2": {"name": "🔥 სრული პაკეტი (5 სესია)",     "price": "455€", "desc": "5 კვირა, 5 სესია."},
    "3": {"name": "🌊 კუნდალინი აქტივაცია",        "price": "222€", "desc": "სასისოცხლო ენერგიის გააქტიურება."},
    "4": {"name": "🚀 1-თვიანი მენტორობა",         "price": "1111€","desc": "კვირაში 2 შეხვედრა."},
}
COURSES = {
    "1": {"name": "👸 ფემინური სიმდიდრე",          "price": "222€", "desc": "5-კვირიანი ონლაინ ტრანსფორმაცია."},
    "2": {"name": "🧘‍♀️ იკიგაი — ცხოვრების აზრი", "price": "290€", "desc": "აღმოაჩინე შენი მისია."},
    "3": {"name": "❤️ თვითსიყვარული და საზღვრები","price": "190€", "desc": "ისწავლე საკუთარი თავის მიღება."},
}

# ─── Helper: send notification to admin ────────────────────────────────────────
async def notify_admin(text: str):
    try:
        await bot.send_message(ADMIN_CHAT_ID, text, parse_mode="HTML")
    except Exception as e:
        logging.error(f"Admin notify error: {e}")

# ─── /start ────────────────────────────────────────────────────────────────────
@dp.message(Command("start"))
async def cmd_start(m: types.Message):
    await m.answer(
        "✨ მოგესალმებით <b>Wonderlander Wellness</b>-ში!\n\n"
        "აირჩიეთ ნებისმიერი სექცია ქვემოთ ⬇️",
        reply_markup=kb.get_main_menu(),
        parse_mode="HTML"
    )

# ─── Sections ──────────────────────────────────────────────────────────────────
@dp.message(F.text == "🌟 სერვისები")
async def show_services(m: types.Message):
    await m.answer("💫 ჩვენი სერვისები — აირჩიეთ:", reply_markup=kb.get_services_keyboard())

@dp.message(F.text == "📚 კურსები")
async def show_courses(m: types.Message):
    await m.answer("📚 ჩვენი კურსები — აირჩიეთ:", reply_markup=kb.get_courses_keyboard())

@dp.message(F.text == "📞 კონტაქტი")
async def show_contact(m: types.Message):
    await m.answer(
        "📍 <b>კონტაქტი</b>\n\n"
        "📧 dr.guranda8@gmail.com\n"
        "📱 WhatsApp: https://wa.me/995597718467\n"
        "📱 Telegram: @wonderlanderr\n"
        "📸 Instagram: wonderlanderwellness",
        parse_mode="HTML"
    )

@dp.message(F.text == "🌐 ენა / Language")
async def show_langs(m: types.Message):
    await m.answer("Choose language / ენა:", reply_markup=kb.get_language_keyboard())

# ─── Service details ───────────────────────────────────────────────────────────
@dp.callback_query(F.data.startswith("service_"))
async def s_details(c: types.CallbackQuery):
    s = SERVICES.get(c.data.split("_")[1])
    if not s:
        return await c.answer("სერვისი ვერ მოიძებნა")
    await c.message.edit_text(
        f"✨ <b>{s['name']}</b>\n"
        f"💰 ფასი: <b>{s['price']}</b>\n\n"
        f"📋 {s['desc']}",
        parse_mode="HTML",
        reply_markup=kb.get_payment_keyboard(s['price'], "service", c.data.split("_")[1])
    )

# ─── Course details ────────────────────────────────────────────────────────────
@dp.callback_query(F.data.startswith("course_"))
async def c_details(c: types.CallbackQuery):
    course = COURSES.get(c.data.split("_")[1])
    if not course:
        return await c.answer("კურსი ვერ მოიძებნა")
    await c.message.edit_text(
        f"📚 <b>{course['name']}</b>\n"
        f"💰 ფასი: <b>{course['price']}</b>\n\n"
        f"📋 {course['desc']}",
        parse_mode="HTML",
        reply_markup=kb.get_payment_keyboard(course['price'], "course", c.data.split("_")[1])
    )

# ─── Back buttons ──────────────────────────────────────────────────────────────
@dp.callback_query(F.data == "back_to_main")
async def b_main(c: types.CallbackQuery):
    await c.message.delete()
    await c.message.answer("მთავარი მენიუ:", reply_markup=kb.get_main_menu())

@dp.callback_query(F.data == "back_to_services")
async def b_services(c: types.CallbackQuery):
    await c.message.edit_text("💫 სერვისები — აირჩიეთ:", reply_markup=kb.get_services_keyboard())

@dp.callback_query(F.data == "back_to_courses")
async def b_courses(c: types.CallbackQuery):
    await c.message.edit_text("📚 კურსები — აირჩიეთ:", reply_markup=kb.get_courses_keyboard())

@dp.callback_query(F.data.startswith("pay_"))
async def process_pay(c: types.CallbackQuery):
    await c.answer("💳 გადახდის სისტემა მალე გაიხსნება!", show_alert=True)

# ─── Booking FSM ───────────────────────────────────────────────────────────────
@dp.message(F.text == "📅 ჩაწერა")
async def start_booking(m: types.Message, state: FSMContext):
    await state.set_state(BookingState.waiting_for_name)
    await m.answer(
        "📝 <b>ჩაწერის ფორმა</b>\n\n"
        "გთხოვთ, შეიყვანეთ თქვენი <b>სახელი და გვარი</b>:",
        parse_mode="HTML"
    )

@dp.message(BookingState.waiting_for_name)
async def process_name(m: types.Message, state: FSMContext):
    await state.update_data(name=m.text)
    await state.set_state(BookingState.waiting_for_phone)
    await m.answer(
        f"✅ მადლობა, <b>{m.text}</b>!\n\n"
        "შეიყვანეთ თქვენი <b>ტელეფონის ნომერი</b> (მაგ: +995599123456):",
        parse_mode="HTML"
    )

@dp.message(BookingState.waiting_for_phone)
async def process_phone(m: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()

    name = data.get("name", "—")
    phone = m.text
    username = f"@{m.from_user.username}" if m.from_user.username else "—"

    # Confirm to user
    await m.answer(
        f"🎉 <b>განაცხადი მიღებულია!</b>\n\n"
        f"👤 სახელი: {name}\n"
        f"📱 ტელეფონი: {phone}\n\n"
        f"⏳ გურანდა მალე დაგიკავშირდებათ! ✨",
        parse_mode="HTML",
        reply_markup=kb.get_main_menu()
    )

    # Notify admin
    await notify_admin(
        f"🔔 <b>ახალი განაცხადი ბოტიდან!</b>\n\n"
        f"👤 სახელი: <b>{name}</b>\n"
        f"📱 ტელეფონი: <b>{phone}</b>\n"
        f"🆔 Telegram: {username}\n"
        f"🔗 User ID: {m.from_user.id}"
    )

# ─── Run ───────────────────────────────────────────────────────────────────────
async def main():
    logging.info("✅ Wonderlander Bot started!")
    await notify_admin("🟢 <b>ბოტი ჩაირთო!</b> Wonderlander Wellness Bot is running.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
