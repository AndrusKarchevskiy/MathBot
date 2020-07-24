from data import db
from loader import dp, types
from aiogram.types.chat import ChatType
from template_messages.users import template_messages as temp_msgs
from keyboards.users.reply import reply_markups
from keyboards.users.inline import inline_markups


@dp.message_handler(ChatType.is_private, commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_username = message.from_user.username
    user_name = message.from_user.full_name
    await db.add_new_user(user_id, user_username, user_name)

    await message.answer(f'<b>Привет, {user_name}</b>!')
    await message.answer(temp_msgs.welcome_message, reply_markup=reply_markups.default_user_markup)


@dp.message_handler(text='📊Алгебра')
async def show_algebra_buttons(message: types.Message):
    await message.answer(temp_msgs.choose_message,
                         reply_markup=inline_markups.algebra_markup)


@dp.message_handler(text='📐Геометрия')
async def show_geometry_buttons(message: types.Message):
    await message.answer(temp_msgs.choose_message, reply_markup=inline_markups.geometry_markup)


@dp.message_handler(text='💹Тригонометрия')
async def show_trigonometry_buttons(message: types.Message):
    await message.answer(temp_msgs.choose_message, reply_markup=inline_markups.trigonometry_markup)


@dp.message_handler(text='👊Посчитать')
async def show_count_buttons(message: types.Message):
    await message.answer(temp_msgs.choose_message, reply_markup=inline_markups.counter_markup)


@dp.callback_query_handler(text_contains='algebra')
@dp.callback_query_handler(text_contains='geometry')
@dp.callback_query_handler(text_contains='trigonometry')
async def send_algebra_media(call: types.CallbackQuery):
    file_path = f'files/{call.data}.png'
    await call.message.answer_photo(open(file_path, 'rb'))
    await call.message.edit_reply_markup(reply_markup=None)
