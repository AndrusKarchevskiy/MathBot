import math

from math_solver import wrong_args
from template_messages.users import template_messages as tmp_msgs


def calculate_expression(expression: str) -> str:
    for sign in expression:
        if sign in wrong_args.BAD_SIGNS:
            return tmp_msgs.not_correct_param

    try:
        expression = str(expression)
        result_of_expression = f'Результат: <b>{eval(expression)}</b>'
    except:
        result_of_expression = tmp_msgs.not_correct_param
    return result_of_expression


def calculate_discriminant(arg_a: float, arg_b: float, arg_c: float) -> str:
    try:
        discriminant = arg_b ** 2 - (4 * arg_a * arg_c)
        if discriminant < 0:
            result_of_calc = 'Дискриминант отрицательный, <b>действительных корней нет</b>'
        else:
            x1 = (-arg_b + discriminant**0.5) / (2 * arg_a)
            x2 = (-arg_b - discriminant**0.5) / (2 * arg_a)

            result_of_calc = f'Дискриминант: <b>{discriminant}</b>\n' \
                             f'Корень из дискриминанта: <b>{discriminant**0.5}</b>\n' \
                             f'Результат 1: <b>{x1}</b>\n' \
                             f'Результат 2: <b>{x2}</b>'
    except:
        result_of_calc = tmp_msgs.not_correct_param

    return result_of_calc


def calculate_sqr(arg_a: float, arg_b: float) -> str:
    try:
        result_of_calc = f'Результат: <b>{arg_a ** arg_b}</b>'
    except:
        result_of_calc = tmp_msgs.not_correct_param
    return result_of_calc


def calculate_sqrt(arg: float) -> str:
    try:
        result_of_calc = f'Результат: <b>{arg ** 0.5}</b>'
    except:
        result_of_calc = tmp_msgs.not_correct_param
    return result_of_calc


def calculate_factorial(arg: int) -> str:
    try:
        factorial = 1
        for multiplier in range(2, arg+1):
            factorial *= multiplier
        result_of_calc = f'Результат: <b>{factorial}</b>'
    except:
        result_of_calc = tmp_msgs.not_correct_param
    return result_of_calc


def calculate_prime(arg: float) -> str:
    try:
        result_of_calc = f'<b>{arg} -- Простое число</b>'
        for i in range(2, math.floor(arg ** 0.5 + 2)):
            if arg % i == 0:
                result_of_calc = result_of_calc.replace('Простое число', 'Составное число')
                break
    except:
        result_of_calc = tmp_msgs.not_correct_param
    return result_of_calc


def calculate_gcd(arg_a: float, arg_b: float) -> str:
    try:
        while arg_a != arg_b:
            if arg_a > arg_b:
                arg_a -= arg_b
            else:
                arg_b -= arg_a
        result_of_calc = f'Результат: <b>{arg_a}</b>'
    except:
        result_of_calc = tmp_msgs.not_correct_param
    return result_of_calc


def calculate_lardiv(arg: float) -> str:
    try:
        if arg == 0:
            max_divisor = 0
        elif arg < 0:
            i = -1
            max_divisor = -1
            while i > arg:
                if arg % i == 0:
                    if i < max_divisor:
                        max_divisor = i
                i -= 1
        else:
            i = 1
            max_divisor = 1
            while i < arg:
                if arg % i == 0:
                    if i > max_divisor:
                        max_divisor = i
                i += 1
        result_of_calc = f'Результат: <b>{max_divisor}</b>'
    except:
        result_of_calc = tmp_msgs.not_correct_param
    return result_of_calc
