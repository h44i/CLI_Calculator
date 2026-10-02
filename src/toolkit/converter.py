from decimal import (
    Decimal,
    getcontext,
    ROUND_HALF_UP,
)

from toolkit.errors import (
    Incompatible_Units_Error,
    Invalid_Temperature_Error,
    Unknown_Unit_Error,
)

# 10 значащих нулей и округление 5>=
getcontext().prec = 10
getcontext().rounding = ROUND_HALF_UP


# конвертация значения из одной единицы измерения в другую
def convert(value: Decimal, from_unit: str, to_unit: str) -> float:
    from_unit, to_unit = from_unit.lower(), to_unit.lower()
    length = {
        "mm": Decimal("0.001"),
        "cm": Decimal("0.01"),
        "m": Decimal("1.0"),
        "km": Decimal("1000.0"),
    }
    mass = {"g": Decimal("0.001"), "kg": Decimal("1.0")}
    temp = {"c", "f", "k"}

    # проверка существования единиц
    if (
        from_unit not in length.keys() | mass.keys() | temp
        or to_unit not in length.keys() | mass.keys() | temp
    ):
        raise Unknown_Unit_Error("Неизвестная единица")

    # перевод единиц длины
    elif from_unit in length and to_unit in length:
        return float(value * length[from_unit] / length[to_unit])

    # перевод единиц массы
    elif from_unit in mass and to_unit in mass:
        return float(value * mass[from_unit] / mass[to_unit])

    # перевод единиц температуры
    elif from_unit in temp and to_unit in temp:
        c = to_c(value, from_unit)
        if c < Decimal("-273.15"):
            raise Invalid_Temperature_Error("Температура ниже абсолютного нуля")

        return float(from_c(c, to_unit))

    else:
        raise Incompatible_Units_Error("Разная группа единиц")


# перевод температуры из указанной единицы в цельсия
def to_c(value: Decimal, to_unit: str) -> Decimal:
    if to_unit == "c":
        return value
    elif to_unit == "f":
        return (value - Decimal("32")) * Decimal("5") / Decimal("9")
    elif to_unit == "k":
        return value - Decimal("273.15")
    raise Unknown_Unit_Error("Неизвестная единица")


# перевод температуры из градусов цельсия в указанную единицу
def from_c(value: Decimal, to_unit: str) -> Decimal:
    if to_unit == "c":
        return value
    elif to_unit == "f":
        return (value * Decimal("9") / Decimal("5")) + Decimal("32")
    elif to_unit == "k":
        return value + Decimal("273.15")
    raise Unknown_Unit_Error("Неизвестная единица")
