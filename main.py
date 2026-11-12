import asyncio
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, types

load_dotenv()
TOKEN=getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message
async def cmd_start(message: types.Message):
    await message.answer("Привет! я ваш ассистент.")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
