import asyncio
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart

from handlers.user_private import user_private_router

load_dotenv()
TOKEN=getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher()

dp.include_router(user_private_router)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! я ваш ассистент.")

@dp.message()
async def cmd_echo(message: types.Message):
    await message.answer(message.text)


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
