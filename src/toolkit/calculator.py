from decimal import (
    Decimal,
    getcontext,
    ROUND_HALF_UP,
    InvalidOperation,
)

from math import floor
from re import findall

from toolkit.errors import (
    DivisionByZeroError,
    EmptyExpressionError,
    InvalidExpressionError,
    InvalidSymbolError,
)

# 10 значащих нулей и округление 5>=
getcontext().prec = 10
getcontext().rounding = ROUND_HALF_UP


# токенизация выражения
def tokenization(s: str) -> list:
    # проверка входных данных
    if not s.strip():
        raise EmptyExpressionError("Пустое выражение")

    for i in s:
        if i not in "0123456789.+-*/% ":
            raise InvalidSymbolError("Недопустимый символ")

    # разбиение выражения на токены с помощью регулярного выражения
    r = r"//|%|[-+*/]|[0-9]+[.][0-9]*|[.][0-9]+|[0-9]+"
    token = findall(r, s)

    # объединение унарных знаков с числами
    for i in range(len(token) - 2, -1, -1):
        # проверка через соседние токены
        if (
            token[i] in "+-"
            and (i == 0 or is_operator(token[i - 1]))
            and is_number(token[i + 1])
        ):
            token[i : i + 2] = [token[i] + token[i + 1]]

    return token


# проверка, является ли токен числом
def is_number(token: str) -> bool:
    # True, если токен можно преобразовать в Decimal иначе False
    try:
        Decimal(token)
        return True
    except InvalidOperation:
        return False


# проверка, является ли токен оператором
def is_operator(token: str) -> bool:
    # True, если токен является оператором иначе False
    return token in {"+", "-", "*", "/", "%", "//"}


# проверка корректности последовательности токенов
def validation(token: list) -> None:
    # проверяет, что выражение не начинается и не заканчивается оператором
    # а также что два числа или два оператора не идут подряд
    if is_operator(token[0]):
        raise InvalidExpressionError("Не может начинаться с оператора")

    elif is_operator(token[-1]):
        raise InvalidExpressionError("Не может заканчиваться оператором")

    for i in range(len(token) - 1):
        if is_number(token[i]) and is_number(token[i + 1]):
            raise InvalidExpressionError("Два числа подряд")

        elif is_operator(token[i]) and is_operator(token[i + 1]):
            raise InvalidExpressionError("Два оператора подряд")


# вычисление операций с высоким приоритетом
def find_first_operator(token: list) -> list:
    # если нашелся оператор с высоким приоритетом, то его левый и правый операнды
    # заменяются результатом операции
    i = 1
    while i < len(token) - 1:
        match token[i]:
            case "*":
                res = Decimal(token[i - 1]) * Decimal(token[i + 1])
                token[i - 1 : i + 2] = [str(res)]

            case "/":
                if Decimal(token[i + 1]) == 0:
                    raise DivisionByZeroError("Деление на ноль")
                res = Decimal(token[i - 1]) / Decimal(token[i + 1])
                token[i - 1 : i + 2] = [str(res)]

            case "//":
                if Decimal(token[i + 1]) == 0:
                    raise DivisionByZeroError("Деление на ноль")
                res = Decimal(token[i - 1]) // Decimal(token[i + 1])
                token[i - 1 : i + 2] = [str(res)]

            case "%":
                a = Decimal(token[i - 1])
                b = Decimal(token[i + 1])
                if b == 0:
                    raise DivisionByZeroError("Деление на ноль")

                res = a - Decimal(floor(a / b)) * b
                token[i - 1 : i + 2] = [str(res)]

            case _:
                i += 1

    return token


# вычисление оставшихся операций (сложение и вычитание)
def calculation(token: list) -> Decimal:
    token = find_first_operator(token)
    res = Decimal(token[0])

    for i in range(1, len(token), 2):
        op = token[i]
        num = Decimal(token[i + 1])

        if op == "+":
            res += num

        elif op == "-":
            res -= num

    return res


# основная функция вычисления выражения
def evaluate(s: str) -> float:
    token = tokenization(s)
    validation(token)

    return float(calculation(token))
