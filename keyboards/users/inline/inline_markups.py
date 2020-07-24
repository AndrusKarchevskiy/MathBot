from aiogram import types


algebra_markup = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text='Формулы сокращённого умножения', callback_data='algebra/multiplication'),
        ],
        [
            types.InlineKeyboardButton(text='Формулы прогрессий', callback_data='algebra/progression')
        ],
        [
            types.InlineKeyboardButton(text='Виды функций (гипербола, парабола и др.)', callback_data='algebra/functions')
        ],
    ]
)

geometry_markup = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text='Площади фигур', callback_data='geometry/figures')
        ],
        [
            types.InlineKeyboardButton(text='Стереометрия (многогранники)', callback_data='geometry/stereometry')
        ],
        [
            types.InlineKeyboardButton(text='Пифагоровы тройки', callback_data='geometry/pythagorean_triples')
        ],
    ]
)

trigonometry_markup = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Основные формулы", callback_data='trigonometry/formulas')
        ],
        [
            types.InlineKeyboardButton(text="Основные тождества логарифмов", callback_data='trigonometry/log')
        ],
        [
            types.InlineKeyboardButton(text="Тригонометрический круг", callback_data='trigonometry/circle')
        ],
        [
            types.InlineKeyboardButton(text="Градусные меры значений sin, cos", callback_data='trigonometry/table')
        ],
        [
            types.InlineKeyboardButton(text="Определения sin, cos, tg", callback_data='definitions')
        ],
        [
            types.InlineKeyboardButton(text="Формулы производной", callback_data='trigonometry/derivative')
        ],
        [
            types.InlineKeyboardButton(text="Формулы приведения", callback_data='trigonometry/reduction_formulas')
        ],
    ]
)

counter_markup = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Значение выражения", callback_data='expression')
        ],
        [
            types.InlineKeyboardButton(text="Дискриминант", callback_data='discriminant')
        ],
        [
            types.InlineKeyboardButton(text="Возведение в степень", callback_data='sqr')
        ],
        [
            types.InlineKeyboardButton(text="Квадратный корень", callback_data='sqrt')
        ],
        [
            types.InlineKeyboardButton(text="Факториал", callback_data='factorial')
        ],
        [
            types.InlineKeyboardButton(text="Простое ли число?", callback_data='prime')
        ],
        [
            types.InlineKeyboardButton(text="Наибольший общий делитель", callback_data='gcd')
        ],
        [
            types.InlineKeyboardButton(text="Наибольший делитель числа", callback_data='lardiv')
        ],
    ]
)
