import asyncio
import logging
from aiogram.filters import BaseFilter
from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
)

from core.models import BotSettings, Service, Course, ContactInfo

logger = logging.getLogger(__name__)

# ─── FSM States ───────────────────────────────────────────────────────────────

class BookingState(StatesGroup):
    waiting_for_name  = State()
    waiting_for_phone = State()


# ─── DB helpers ───────────────────────────────────────────────────────────────

@sync_to_async
def get_settings():
    return BotSettings.objects.first()

@sync_to_async
def get_services():
    return list(Service.objects.filter(is_active=True).order_by('order'))

@sync_to_async
def get_courses():
    return list(Course.objects.filter(is_active=True))

@sync_to_async
def get_contact_info():
    return ContactInfo.objects.first()


# ─── UI helpers ───────────────────────────────────────────────────────────────

def build_main_menu(s):
    """s = BotSettings instance"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=s.btn_services), KeyboardButton(text=s.btn_courses)],
            [KeyboardButton(text=s.btn_booking),  KeyboardButton(text=s.btn_contact)],
            [KeyboardButton(text=s.btn_language)],
        ],
        resize_keyboard=True,
    )


async def notify_admin(bot: Bot, text: str):
    s = await get_settings()
    if s and s.admin_chat_id:
        try:
            await bot.send_message(s.admin_chat_id, text, parse_mode="HTML")
        except Exception as e:
            logger.error(f"Admin notify error: {e}")


# ─── Filter ───────────────────────────────────────────────────────────────────

class BtnFilter(BaseFilter):
    """Match message.text against a BotSettings button field (async, DB-backed)."""

    def __init__(self, field: str):
        self.field = field

    async def __call__(self, message: types.Message) -> bool:
        if not message.text:
            return False
        cfg = await get_settings()
        if not cfg:
            return False
        return message.text == getattr(cfg, self.field, '')


# ─── Dispatcher (module-level) ────────────────────────────────────────────────

dp = Dispatcher()


# ─── /start ───────────────────────────────────────────────────────────────────

@dp.message(Command("start"))
async def cmd_start(m: types.Message):
    cfg = await get_settings()
    await m.answer(cfg.welcome_text_ge, reply_markup=build_main_menu(cfg), parse_mode="HTML")


# ─── Main menu buttons ────────────────────────────────────────────────────────

@dp.message(BtnFilter('btn_services'))
async def show_services(m: types.Message):
    cfg = await get_settings()
    services = await get_services()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{sv.icon} {sv.title_ge}", callback_data=f"srv_{sv.id}")]
        for sv in services
    ] + [[InlineKeyboardButton(text=cfg.btn_back, callback_data="back_main")]])
    await m.answer(cfg.services_menu_text_ge, reply_markup=kb)


@dp.message(BtnFilter('btn_courses'))
async def show_courses(m: types.Message):
    cfg = await get_settings()
    courses = await get_courses()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=c.title_ge, callback_data=f"crs_{c.id}")]
        for c in courses
    ] + [[InlineKeyboardButton(text=cfg.btn_back, callback_data="back_main")]])
    await m.answer(cfg.courses_menu_text_ge, reply_markup=kb)


@dp.message(BtnFilter('btn_contact'))
async def show_contact(m: types.Message):
    cfg = await get_settings()
    contact = await get_contact_info()
    text = cfg.contact_text_ge
    if contact:
        if contact.whatsapp:   text += f"\n📱 WhatsApp: {contact.whatsapp}"
        if contact.telegram:   text += f"\n✈️ Telegram: {contact.telegram}"
        if contact.instagram:  text += f"\n📸 Instagram: {contact.instagram}"
        if contact.email:      text += f"\n📧 Email: {contact.email}"
    await m.answer(text, parse_mode="HTML")


@dp.message(BtnFilter('btn_language'))
async def show_language(m: types.Message):
    cfg = await get_settings()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=cfg.btn_language_ge, callback_data="lang_ge")],
        [InlineKeyboardButton(text=cfg.btn_language_en, callback_data="lang_en")],
        [InlineKeyboardButton(text=cfg.btn_back,        callback_data="back_main")],
    ])
    await m.answer(cfg.language_choice_text, reply_markup=kb)


# ─── Booking (FSM) ────────────────────────────────────────────────────────────

@dp.message(BtnFilter('btn_booking'))
async def booking_start(m: types.Message, state: FSMContext):
    cfg = await get_settings()
    await state.set_state(BookingState.waiting_for_name)
    await m.answer(cfg.booking_ask_name, parse_mode="HTML")


@dp.message(StateFilter(BookingState.waiting_for_name))
async def booking_name(m: types.Message, state: FSMContext):
    cfg = await get_settings()
    await state.update_data(name=m.text)
    await state.set_state(BookingState.waiting_for_phone)
    await m.answer(
        cfg.booking_ask_phone.replace("{name}", f"<b>{m.text}</b>"),
        parse_mode="HTML",
    )


@dp.message(StateFilter(BookingState.waiting_for_phone))
async def booking_phone(m: types.Message, state: FSMContext):
    cfg = await get_settings()
    data  = await state.get_data()
    await state.clear()
    name     = data.get("name", "—")
    phone    = m.text
    username = f"@{m.from_user.username}" if m.from_user.username else "—"

    await m.answer(cfg.booking_success_text_ge, parse_mode="HTML", reply_markup=build_main_menu(cfg))

    # notify admin — bot object is retrieved from context
    bot: Bot = m.bot
    await notify_admin(
        bot,
        f"{cfg.booking_admin_notify}\n\n"
        f"👤 სახელი: <b>{name}</b>\n"
        f"📱 ტელეფონი: <b>{phone}</b>\n"
        f"🆔 Telegram: {username}\n"
        f"🔗 User ID: {m.from_user.id}",
    )


# ─── Inline callbacks ─────────────────────────────────────────────────────────

@dp.callback_query(F.data.startswith("srv_"))
async def service_detail(c: types.CallbackQuery):
    cfg     = await get_settings()
    srv_id  = int(c.data.split("_")[1])
    services = await get_services()
    sv = next((x for x in services if x.id == srv_id), None)
    if not sv:
        return await c.answer(cfg.not_found_text)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{cfg.btn_pay_label} ({sv.price})", callback_data=f"pay_srv_{sv.id}")],
        [InlineKeyboardButton(text=cfg.btn_back, callback_data="back_services")],
    ])
    desc = sv.short_description_ge or (sv.description_ge[:200] if sv.description_ge else "")
    await c.message.edit_text(
        f"✨ <b>{sv.title_ge}</b>\n💰 {sv.price}\n⏱ {sv.duration}\n\n{desc}",
        parse_mode="HTML", reply_markup=kb,
    )


@dp.callback_query(F.data.startswith("crs_"))
async def course_detail(c: types.CallbackQuery):
    cfg    = await get_settings()
    crs_id = int(c.data.split("_")[1])
    courses = await get_courses()
    crs = next((x for x in courses if x.id == crs_id), None)
    if not crs:
        return await c.answer(cfg.not_found_text)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{cfg.btn_pay_label} ({crs.total_value_ge})", callback_data=f"pay_crs_{crs.id}")],
        [InlineKeyboardButton(text=cfg.btn_back, callback_data="back_courses")],
    ])
    desc = crs.subtitle_ge or (crs.description_ge[:200] if crs.description_ge else "")
    await c.message.edit_text(
        f"📚 <b>{crs.title_ge}</b>\n💰 {crs.total_value_ge}\n\n{desc}",
        parse_mode="HTML", reply_markup=kb,
    )


@dp.callback_query(F.data.startswith("pay_"))
async def pay_handler(c: types.CallbackQuery):
    cfg = await get_settings()
    await c.answer(cfg.payment_soon_text, show_alert=True)


@dp.callback_query(F.data.startswith("lang_"))
async def lang_handler(c: types.CallbackQuery):
    cfg  = await get_settings()
    lang = c.data.split("_")[1]
    msg  = "🇬🇪 ქართული ენა არჩეულია!" if lang == "ge" else "🇬🇧 English selected!"
    await c.message.delete()
    await c.message.answer(msg, reply_markup=build_main_menu(cfg))


@dp.callback_query(F.data == "back_main")
async def back_main(c: types.CallbackQuery):
    cfg = await get_settings()
    await c.message.delete()
    await c.message.answer(cfg.welcome_text_ge, reply_markup=build_main_menu(cfg), parse_mode="HTML")


@dp.callback_query(F.data == "back_services")
async def back_services(c: types.CallbackQuery):
    cfg      = await get_settings()
    services = await get_services()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{sv.icon} {sv.title_ge}", callback_data=f"srv_{sv.id}")]
        for sv in services
    ] + [[InlineKeyboardButton(text=cfg.btn_back, callback_data="back_main")]])
    await c.message.edit_text(cfg.services_menu_text_ge, reply_markup=kb)


@dp.callback_query(F.data == "back_courses")
async def back_courses(c: types.CallbackQuery):
    cfg     = await get_settings()
    courses = await get_courses()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=crs.title_ge, callback_data=f"crs_{crs.id}")]
        for crs in courses
    ] + [[InlineKeyboardButton(text=cfg.btn_back, callback_data="back_main")]])
    await c.message.edit_text(cfg.courses_menu_text_ge, reply_markup=kb)


# ─── Django management command ────────────────────────────────────────────────

class Command(BaseCommand):
    help = 'Runs the Telegram bot (integrated with Django DB)'

    def handle(self, *args, **options):
        self.stdout.write("Starting Wonderlander Bot...")
        asyncio.run(self.run_bot())

    async def run_bot(self):
        s = await get_settings()
        if not s or not s.bot_token:
            self.stderr.write("ERROR: Bot Token not found in Admin › ბოტის პარამეტრები")
            return

        bot = Bot(token=s.bot_token)
        self.stdout.write(self.style.SUCCESS("Wonderlander Bot is running!"))
        await notify_admin(bot, s.bot_started_text)
        await dp.start_polling(bot)
