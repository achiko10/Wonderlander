import sys
import os
import asyncio

project_dir = r'c:\Users\Utente\.gemini\antigravity\scratch\wonderlander_wellness'
sys.path.insert(0, project_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from core.management.commands.runbot import Command
from aiogram import types

async def test():
    cmd = Command()
    # We want to run cmd.run_bot(), but it will start polling forever.
    # So we will monkeypatch dp.start_polling
    from aiogram import Dispatcher
    original_start_polling = Dispatcher.start_polling
    
    async def fake_start_polling(self, *bots, **kwargs):
        print("Bot is started! Feeding /start update...")
        try:
            update = types.Update(update_id=1, message=types.Message(message_id=1, date=1, chat=types.Chat(id=1, type="private"), text="/start"))
            await self.feed_update(bots[0], update)
            print("Update processed successfully!")
        except Exception as e:
            import traceback
            traceback.print_exc()
            
    Dispatcher.start_polling = fake_start_polling
    await cmd.run_bot()

if __name__ == "__main__":
    asyncio.run(test())
