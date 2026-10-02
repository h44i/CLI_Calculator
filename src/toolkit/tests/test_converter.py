import pytest
from toolkit.converter import convert
from toolkit.errors import (
    IncompatibleUnitsError,
    InvalidTemperatureError,
    UnknownUnitError,
)


def test_1():
    assert convert(1000, "mm", "m") == 1.0


def test_2():
    assert convert(10, "kg", "g") == 10000.0


def test_3():
    assert convert(200, "c", "f") == 392.0


def test_UnknownUnit():
    with pytest.raises(UnknownUnitError):
        convert(10, "mm", "x")


def test_IncompatibleUnits():
    with pytest.raises(IncompatibleUnitsError):
        convert(10, "mm", "kg")


def test_InvalidTemperature():
    with pytest.raises(InvalidTemperatureError):
        convert(-300, "c", "k")
