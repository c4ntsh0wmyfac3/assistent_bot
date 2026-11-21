import asyncio
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart

from handlers.user_private import user_private_router
from common.bot_cmds import private

load_dotenv()
TOKEN=getenv('TOKEN')
ALLOWED_UPDATES=['message', 'edited_message']
bot = Bot(TOKEN)
dp = Dispatcher()

dp.include_router(user_private_router)

async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == '__main__':
    asyncio.run(main())
