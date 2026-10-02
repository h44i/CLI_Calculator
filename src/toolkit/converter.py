from toolkit.errors import (
    IncompatibleUnitsError,
    InvalidTemperatureError,
    UnknownUnitError,
)


# конвертация значения из одной единицы измерения в другую
def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit, to_unit = from_unit.lower(), to_unit.lower()
    length = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
    mass = {"g": 0.001, "kg": 1.0}
    temp = {"c", "f", "k"}

    # проверка существования единиц
    if (
        from_unit not in length.keys() | mass.keys() | temp
        or to_unit not in length.keys() | mass.keys() | temp
    ):
        raise UnknownUnitError("Неизвестная единица")

    # перевод единиц длины
    elif from_unit in length and to_unit in length:
        return value * length[from_unit] / length[to_unit]

    # перевод единиц массы
    elif from_unit in mass and to_unit in mass:
        return value * mass[from_unit] / mass[to_unit]

    # перевод единиц температуры
    elif from_unit in temp and to_unit in temp:
        c = to_c(value, from_unit)
        if c < -273.15:
            raise InvalidTemperatureError("Температура ниже абсолютного нуля")

        return from_c(c, to_unit)

    else:
        raise IncompatibleUnitsError("Разная группа единиц")


# перевод температуры из указанной единицы в цельсия
def to_c(value: float, to_unit: str) -> float:
    if to_unit == "c":
        return value
    elif to_unit == "f":
        return (value - 32) * 5 / 9
    elif to_unit == "k":
        return value - 273


# перевод температуры из градусов цельсия в указанную единицу
def from_c(value: float, to_unit: str) -> float:
    if to_unit == "c":
        return value
    elif to_unit == "f":
        return (value * 9 / 5) + 32
    elif to_unit == "k":
        return value + 273
