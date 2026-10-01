from re import findall
from decimal import Decimal, InvalidOperation
from toolkit.errors import (
    EmptyExpressionError, 
    InvalidExpressionError, 
    DivisionByZeroError, 
    InvalidSymbolError,
)


# токенизация
def tokenization(s: str) -> list:
    # проверка ошибок
    if not s.strip():
        raise EmptyExpressionError("Пустое выражение")
    
    for i in s:
        if i not in "0123456789.+-*/% ":
            raise InvalidSymbolError("Недопустимый символ")

    # регулярка
    r = r'//|%|[-+*/]|[0-9]+[.][0-9]+|[0-9]+'
    token = findall(r, s)

    # поиск унарного минуса/плюса
    for i in range(len(token) - 2, -1, -1):
        if (
            token[i] in '+-' 
            and (i == 0 or is_operator(token[i-1])) 
            and is_number(token[i+1])
        ):
            token[i:i+2] = [token[i] + token[i+1]]
            
    return token


# проверка что токен это число
def is_number(token: str) -> bool:
    try:
        Decimal(token)
        return True
    except InvalidOperation:
        return False


# проверка что токен это оператор
def is_operator(token: str) -> bool:
    return token in {"+", "-", "*", "/", "%", "//"}


# проверка токенизированного списка
def validation(token: list) -> None:
    # проверка ошибок
    if is_operator(token[0]):
        raise InvalidExpressionError("Не может начинаться с оператора")
    
    elif is_operator(token[-1]):
        raise InvalidExpressionError("Не может заканчиваться оператором")

    for i in range(len(token)-1):
        if is_number(token[i]) and is_number(token[i+1]):
            raise InvalidExpressionError("Два числа подряд")
        
        elif is_operator(token[i]) and is_operator(token[i+1]):
             raise InvalidExpressionError("Два оператора подряд")


# ищем умножение или деление потом замена среза на конечное значение
def find_first_operator(token: list) -> list:
    i = 1
    while i < len(token) - 1:
        match token[i]:
            case "*":
                res = Decimal(token[i-1]) * Decimal(token[i+1])
                token[i-1:i+2] = [str(res)]

            case "/":
                if Decimal(token[i+1]) == 0:
                    raise DivisionByZeroError("Деление на ноль")
                res = Decimal(token[i-1]) / Decimal(token[i+1])
                token[i-1:i+2] = [str(res)]

            case "//":
                if Decimal(token[i+1]) == 0:
                    raise DivisionByZeroError("Деление на ноль")
                res = Decimal(token[i-1]) // Decimal(token[i+1])
                token[i-1:i+2] = [str(res)]

            case "%":
                if Decimal(token[i+1]) == 0:
                    raise DivisionByZeroError("Деление на ноль")
                res = Decimal(token[i-1]) % Decimal(token[i+1])
                token[i-1:i+2] = [str(res)]
                
            case _:
                i += 1
            
    return token


# подсчет листа
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


# конечный вывод
def evaluate(s: str) -> float:
    token = tokenization(s)
    validation(token)
    
    return float(calculation(token))