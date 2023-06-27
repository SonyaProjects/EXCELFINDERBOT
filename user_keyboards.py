from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/help')
        ],
        [
            KeyboardButton(text='/search_by_id'),
            KeyboardButton(text='/search_by_name')
        ]
    ],
    resize_keyboard=True
)
