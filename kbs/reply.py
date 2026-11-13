from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_start = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Заказать Бот"),
                KeyboardButton(text="Часто Задаваемые Вопросы"),
            ],
            [
                KeyboardButton(text="Написать Мне В Личку")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Что пожелаете?"
)
