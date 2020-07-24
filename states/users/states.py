from aiogram.dispatcher.filters.state import StatesGroup, State


class MathExpressions(StatesGroup):
    Expression = State()
    Discriminant = State()
    SetNewsTopic = State()
    Sqr = State()
    Sqrt = State()
    Factorial = State()
    Prime = State()
    Gcd = State()
    LarDiv = State()
