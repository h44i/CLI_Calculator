import pytest
from toolkit.calculator import evaluate
from toolkit.errors import (
    DivisionByZeroError,
    EmptyExpressionError,
    InvalidExpressionError,
)


def test_1():
    assert evaluate("2 + 3") == 5.0


def test_2():
    assert evaluate("2 + 3 * 4") == 14.0


def test_3():
    assert evaluate("10 / 2") == 5.0


def test_4():
    assert evaluate("-5 + 3") == -2.0


def test_5():
    assert evaluate(".1 + .001 + -.3 -1.") == -1.199


def test_6():
    assert evaluate("7 % 5") == 2.0


def test_EmptyExpression():
    with pytest.raises(EmptyExpressionError):
        evaluate("")


def test_DivisionByZero():
    with pytest.raises(DivisionByZeroError):
        evaluate("5 / 0")


def test_InvalidExpression():
    with pytest.raises(InvalidExpressionError):
        evaluate("2 + / 3")
