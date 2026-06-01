import sys
import os

project_dir = r'c:\Users\Utente\.gemini\antigravity\scratch\wonderlander_wellness'
sys.path.insert(0, project_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from core.management.commands.runbot import Command
from aiogram import Bot, Dispatcher, types
import asyncio

async def test():
    cmd = Command()
    # We copy handlers from run_bot
    dp = Dispatcher()
    from aiogram.filters import Command as Cmd, StateFilter
    from core.management.commands.runbot import BtnFilter, BookingState, build_main_menu, get_settings, get_services, get_courses, get_contact_info
    from aiogram import F

    print("Registering handlers...")
    
    @dp.message(Cmd("start"))
    async def cmd_start(m: types.Message): pass

    @dp.message(BtnFilter('btn_services'))
    async def show_services(m: types.Message): pass

    @dp.message(BtnFilter('btn_courses'))
    async def show_courses(m: types.Message): pass

    @dp.message(BtnFilter('btn_contact'))
    async def show_contact(m: types.Message): pass

    @dp.message(BtnFilter('btn_language'))
    async def show_language(m: types.Message): pass

    @dp.callback_query(F.data.startswith("srv_"))
    async def service_detail(c: types.CallbackQuery): pass

    @dp.callback_query(F.data.startswith("crs_"))
    async def course_detail(c: types.CallbackQuery): pass

    @dp.callback_query(F.data.startswith("pay_"))
    async def pay_handler(c: types.CallbackQuery): pass

    @dp.callback_query(F.data.startswith("lang_"))
    async def lang_handler(c: types.CallbackQuery): pass

    @dp.callback_query(F.data == "back_main")
    async def back_main(c: types.CallbackQuery): pass

    @dp.callback_query(F.data == "back_services")
    async def back_services(c: types.CallbackQuery): pass

    @dp.callback_query(F.data == "back_courses")
    async def back_courses(c: types.CallbackQuery): pass

    @dp.message(BtnFilter('btn_booking'))
    async def booking_start(m: types.Message): pass

    @dp.message(StateFilter(BookingState.waiting_for_name))
    async def booking_name(m: types.Message): pass

    @dp.message(StateFilter(BookingState.waiting_for_phone))
    async def booking_phone(m: types.Message): pass

    print("Checking filters...")
    for observer in dp.message.handlers:
        for f in observer.filters:
            c = f.callback
            if not callable(c):
                from aiogram.filters.base import Filter
                if isinstance(c, Filter):
                    pass
                else:
                    print(f"NOT CALLABLE: {c} for handler {observer.callback}")
    
    for observer in dp.callback_query.handlers:
        for f in observer.filters:
            c = f.callback
            if not callable(c):
                from aiogram.filters.base import Filter
                if isinstance(c, Filter):
                    pass
                else:
                    print(f"NOT CALLABLE: {c} for handler {observer.callback}")

    print("Done checking.")

if __name__ == "__main__":
    asyncio.run(test())
