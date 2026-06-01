import sys
import os

project_dir = r'c:\Users\Utente\.gemini\antigravity\scratch\wonderlander_wellness'
sys.path.insert(0, project_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from core.management.commands.runbot import Command
from aiogram import Dispatcher, types
import asyncio

async def test():
    cmd = Command()
    # We just run the setup part
    from core.models import BotSettings
    s = await BotSettings.objects.afirst()
    from aiogram import Bot
    bot = Bot(token="12345:ABCDEF")
    dp = Dispatcher()
    
    # We copy handlers from run_bot
    from aiogram.filters import Command as Cmd, StateFilter
    from core.management.commands.runbot import BtnFilter, BookingState, build_main_menu, get_settings, get_services, get_courses, get_contact_info
    from aiogram import F

    print("Registering /start...")
    @dp.message(Cmd("start"))
    async def cmd_start(m: types.Message): pass

    print("Registering btn_services...")
    try:
        @dp.message(BtnFilter('btn_services'))
        async def show_services(m: types.Message): pass
    except Exception as e:
        print("Error registering btn_services:", e)

    print("Registering StateFilter...")
    try:
        @dp.message(StateFilter(BookingState.waiting_for_name))
        async def booking_name(m: types.Message): pass
    except Exception as e:
        print("Error registering StateFilter:", e)

    print("Simulating update...")
    try:
        update = types.Update(update_id=1, message=types.Message(message_id=1, date=1, chat=types.Chat(id=1, type="private"), text="/start"))
        await dp.feed_update(bot, update)
        print("Update processed successfully!")
    except Exception as e:
        import traceback
        traceback.print_exc()

asyncio.run(test())
