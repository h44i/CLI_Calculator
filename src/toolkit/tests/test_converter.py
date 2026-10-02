import pytest
from toolkit.converter import convert
from toolkit.errors import (
    Incompatible_Units_Error,
    Invalid_Temperature_Error,
    Unknown_Unit_Error,
)


def test_Lenght():
    value, from_unit, to_unit = 1000, "mm", "m"
    result = convert(value, from_unit, to_unit)

    print(f"\n{value} --from {from_unit} --to {to_unit} = {result}")

    assert result == 1.0


def test_Mass():
    value, from_unit, to_unit = 10, "kg", "g"
    result = convert(value, from_unit, to_unit)

    print(f"\n{value} --from {from_unit} --to {to_unit} = {result}")

    assert result == 10000.0


def test_Tempature():
    value, from_unit, to_unit = 200, "c", "f"
    result = convert(value, from_unit, to_unit)

    print(f"\n{value} --from {from_unit} --to {to_unit} = {result}")

    assert result == 392.0


def test_Unknown_Unit():
    value, from_unit, to_unit = 10, "mm", "x"

    print(f"\n{value} --from {from_unit} --to {to_unit} = Unknown_Unit_Error")

    with pytest.raises(Unknown_Unit_Error):
        convert(10, "mm", "x")


def test_Incompatible_Units():
    value, from_unit, to_unit = 10, "mm", "kg"

    print(f"\n{value} --from {from_unit} --to {to_unit} = Incompatible_Units_Error")

    with pytest.raises(Incompatible_Units_Error):
        convert(10, "mm", "kg")


def test_Invalid_Temperature():
    value, from_unit, to_unit = -300, "c", "k"

    print(f"\n{value} --from {from_unit} --to {to_unit} = Invalid_Temperature_Error")

    with pytest.raises(Invalid_Temperature_Error):
        convert(-300, "c", "k")
