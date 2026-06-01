from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="🌟 სერვისები"), KeyboardButton(text="📚 კურსები")],[KeyboardButton(text="📅 ჩაწერა"), KeyboardButton(text="📞 კონტაქტი")],[KeyboardButton(text="🌐 ენა / Language")]], resize_keyboard=True)

def get_services_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="💆‍♀️ ინდივიდუალური სესია", callback_data="service_1")],[InlineKeyboardButton(text="🔥 სრული პაკეტი (5 სესია)", callback_data="service_2")],[InlineKeyboardButton(text="🌊 კუნდალინი აქტივაცია", callback_data="service_3")],[InlineKeyboardButton(text="🚀 1-თვიანი მენტორობა", callback_data="service_4")],[InlineKeyboardButton(text="🔙 უკან", callback_data="back_to_main")]])

def get_courses_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="👸 ფემინური სიმდიდრე", callback_data="course_1")],[InlineKeyboardButton(text="🧘‍♀️ იკიგაი — ცხოვრების აზრი", callback_data="course_2")],[InlineKeyboardButton(text="❤️ თვითსიყვარული და საზღვრები", callback_data="course_3")],[InlineKeyboardButton(text="🔙 უკან", callback_data="back_to_main")]])

def get_payment_keyboard(price, item_type, item_id):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"💳 გადახდა ({price}€)", callback_data=f"pay_{item_type}_{item_id}")],[InlineKeyboardButton(text="🔙 უკან", callback_data=f"back_to_{item_type}s")]])

def get_language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🇬🇪 ქართული", callback_data="lang_ge")],[InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],[InlineKeyboardButton(text="🔙 უკან", callback_data="back_to_main")]])
