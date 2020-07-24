from aiogram.dispatcher import FSMContext

from data import db
from loader import dp, types
from aiogram.types.chat import ChatType
from template_messages.users import template_messages as temp_msgs
from keyboards.users.reply import reply_markups
from keyboards.users.inline import inline_markups
from math_solver import solver
from states.users import states


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
async def send_info_media_files(call: types.CallbackQuery):
    file_path = f'files/{call.data}.png'
    await call.message.answer_photo(open(file_path, 'rb'))
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(text='definitions')
async def send_trigonometry_definitions(call: types.CallbackQuery):
    await call.message.answer('📌<b>Синус —</b> отношение противолежащего катета к гипотенузе\n'
                              '📌<b>Косинус —</b> отношение прилежащего катета к гипотенузе\n'
                              '📌<b>Тангенс —</b> отношение противолежащего катета к '
                              'прилежащему\n'
                              '📌<b>Котангенс —</b> отношение прилежащего катета к '
                              'противолежащему\n'
                              '📌<b>Секанс —</b> отношение гипотенузы к прилежащему катету\n'
                              '📌<b>Косеканс —</b> отношение гипотенузы к противолежащему катету')
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(text='expression')
async def get_expression(call: types.CallbackQuery):
    await call.message.answer('<b>Введите выражение, значение которого будем вычислять</b>')
    await states.MathExpressions.Expression.set()
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(state=states.MathExpressions.Expression)
async def send_result_of_expression(message: types.Message, state: FSMContext):
    expression = message.text
    message_to_user = solver.calculate_expression(expression)
    await message.answer(message_to_user)
    await state.finish()


@dp.callback_query_handler(text='discriminant')
async def get_discriminant_args(call: types.CallbackQuery):
    await call.message.answer('<b>Введите 3 аргумента (a, b, c) через пробел</b>')
    await states.MathExpressions.Discriminant.set()
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(state=states.MathExpressions.Discriminant)
async def send_result_of_discriminant(message: types.Message, state: FSMContext):
    try:
        expression = str(message.text).split(' ')
        arg_a, arg_b, arg_c = float(expression[0]), float(expression[1]), float(expression[2])
        message_to_user = solver.calculate_discriminant(arg_a, arg_b, arg_c)
    except:
        message_to_user = temp_msgs.not_correct_param

    await message.answer(message_to_user)
    await state.finish()


@dp.callback_query_handler(text='sqrt')
async def get_sqrt_args(call: types.CallbackQuery):
    await call.message.answer('<b>Введите число, квадратный корень которого будем вычислять</b>')
    await states.MathExpressions.Sqrt.set()
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(state=states.MathExpressions.Sqrt)
async def send_result_of_sqrt(message: types.Message, state: FSMContext):
    try:
        num = float(message.text)
        message_to_user = solver.calculate_sqrt(num)
    except:
        message_to_user = temp_msgs.not_correct_param

    await message.answer(message_to_user)
    await state.finish()


@dp.callback_query_handler(text='sqr')
async def get_sqr_args(call: types.CallbackQuery):
    await call.message.answer('<b>Введите 2 числа через пробел:</b>\n<i>Первое</i> - число, '
                              'которое будем возводить в степень\n<i>Второе</i> - степень, '
                              'в которую будем возводить в число')
    await states.MathExpressions.Sqr.set()
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(state=states.MathExpressions.Sqr)
async def send_result_of_sqr(message: types.Message, state: FSMContext):
    try:
        expression = str(message.text).split(' ')
        arg_a, arg_b = float(expression[0]), float(expression[1])
        message_to_user = solver.calculate_sqr(arg_a, arg_b)
    except:
        message_to_user = temp_msgs.not_correct_param

    await message.answer(message_to_user)
    await state.finish()


@dp.callback_query_handler(text='factorial')
async def get_factorial_args(call: types.callback_query):
    await call.message.answer('<b>Введите число, факториал которого будем находить</b>')
    await states.MathExpressions.Factorial.set()
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(state=states.MathExpressions.Factorial)
async def send_result_of_factorial(message: types.Message, state: FSMContext):
    try:
        arg = int(message.text)
        message_to_user = solver.calculate_factorial(arg)
    except:
        message_to_user = temp_msgs.not_correct_param

    await message.answer(message_to_user)
    await state.finish()


@dp.callback_query_handler(text='prime')
async def get_prime_args(call: types.callback_query):
    await call.message.answer('<b>Введите число, которое будем проверять</b>')
    await states.MathExpressions.Prime.set()
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(state=states.MathExpressions.Prime)
async def send_result_of_prime(message: types.Message, state: FSMContext):
    try:
        arg = int(message.text)
        message_to_user = solver.calculate_prime(arg)
    except:
        message_to_user = temp_msgs.not_correct_param

    await message.answer(message_to_user)
    await state.finish()


@dp.callback_query_handler(text='gcd')
async def get_gcd_args(call: types.callback_query):
    await call.message.answer('<b>Введите 2 числа через пробел, у которых '
                              'будем искать наибольший общий делитель</b>')
    await states.MathExpressions.Gcd.set()
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(state=states.MathExpressions.Gcd)
async def send_result_of_gcd(message: types.Message, state: FSMContext):
    try:
        expression = str(message.text).split(' ')
        arg_a, arg_b = float(expression[0]), float(expression[1])
        message_to_user = solver.calculate_gcd(arg_a, arg_b)
    except:
        message_to_user = temp_msgs.not_correct_param

    await message.answer(message_to_user)
    await state.finish()


@dp.callback_query_handler(text='lardiv')
async def get_lardiv_args(call: types.callback_query):
    await call.message.answer('<b>Введите число, наибольший делитель которого, '
                              'кроме него самого, будем вычислять</b>')
    await states.MathExpressions.LarDiv.set()
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(state=states.MathExpressions.LarDiv)
async def send_result_of_lardiv(message: types.Message, state: FSMContext):
    try:
        arg = float(message.text)
        message_to_user = solver.calculate_lardiv(arg)
    except:
        message_to_user = temp_msgs.not_correct_param

    await message.answer(message_to_user)
    await state.finish()


@dp.message_handler(ChatType.is_private)
async def wrong_message(message: types.Message):
    await message.answer('Такую команду создатель ещё не завёз 🙃')
