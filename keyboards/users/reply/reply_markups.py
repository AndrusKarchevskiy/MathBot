from aiogram import types


default_user_markup = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='📊Алгебра'),
            types.KeyboardButton(text='📐Геометрия')
        ],
        [
            types.KeyboardButton(text='💹Тригонометрия')
        ],
        [
            types.KeyboardButton(text='👊Посчитать')
        ],
    ],
    resize_keyboard=True
)
