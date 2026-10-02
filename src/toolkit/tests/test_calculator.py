import pytest
from toolkit.calculator import evaluate
from toolkit.errors import (
    Division_By_Zero_Error,
    Empty_Expression_Error,
    Invalid_Expression_Error,
)


def test_Plus():
    expression = "2 + 3"
    result = evaluate(expression)

    print(f"\n{expression} = {result}")

    assert result == 5.0


def test_Operation_Priorities():
    expression = "2 + 3 * 4 / 2"
    result = evaluate(expression)

    print(f"\n{expression} = {result}")

    assert result == 8.0


def test_Integer_Division():
    expression = "9 // 2"
    result = evaluate(expression)

    print(f"\n{expression} = {result}")

    assert result == 4.0


def test_Unary():
    expression = "-5 + 3"
    result = evaluate(expression)

    print(f"\n{expression} = {result}")

    assert result == -2.0


def test_Point_Without_Null():
    expression = ".1 + .001 + -.3 -1."
    result = evaluate(expression)

    print(f"\n{expression} = {result}")

    assert result == -1.199


def test_Negative_Remainder():
    expression = "-7 % 5"
    result = evaluate(expression)

    print(f"\n{expression} = {result}")

    assert result == 3.0


def test_Empty_Expression():
    expression = " "

    print(f"\n[{expression}] = Empty_Expression_Error")

    with pytest.raises(Empty_Expression_Error):
        evaluate(expression)


def test_Division_By_Zero():
    expression = "5 / 0"

    print(f"\n{expression} = Division_By_Zero_Error")

    with pytest.raises(Division_By_Zero_Error):
        evaluate("5 / 0")


def test_Invalid_Expression():
    expression = "2 + / 3"

    print(f"\n{expression} = Invalid_Expression_Error")

    with pytest.raises(Invalid_Expression_Error):
        evaluate(expression)
