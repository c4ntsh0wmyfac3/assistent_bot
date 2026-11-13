from aiogram import F, types, Router
from aiogram.filters import Command, CommandStart, or_f
from filters.chat_types import ChatTypeFilter
from kbs import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Я ваш помощник по вопросам телеграм ботов и автоматизации", reply_markup=reply.kb_start)
