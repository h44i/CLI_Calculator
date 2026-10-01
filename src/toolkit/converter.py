from toolkit.errors import (
    UnknownUnitError, 
    IncompatibleUnitsError, 
    InvalidTemperatureError,
)

def convert(value, from_unit, to_unit):
    from_unit, to_unit = from_unit.lower(), to_unit.lower()
    endvalue = 0
    length = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0}
    mass = {'g': 0.001, 'kg': 1.0}
    temp = {'c', 'f', 'k'}

    # проверка ед.из. через объединение ключей словаря и множества 
    if (
        from_unit not in length.keys() | mass.keys() | temp 
        or to_unit not in length.keys() | mass.keys() | temp
    ):
        raise UnknownUnitError("Неизвестная единица")

    # подсчет
    elif from_unit in length and to_unit in length:
        endvalue = value * length[from_unit] / length[to_unit]

    elif from_unit in mass and to_unit in mass:
        endvalue = value * mass[from_unit] / mass[to_unit]

    elif from_unit in temp and to_unit in temp:
        c = to_c(value, from_unit)
        if c < -273:
            raise InvalidTemperatureError("Температура ниже абсолютного нуля")
            
        return from_c(c, to_unit)
    
    else: raise IncompatibleUnitsError("Разная группа единиц")

    return endvalue

# перевод всех единиц в цельсии
def to_c(value, to_unit):
    if to_unit == 'c':
        return value
    elif to_unit == 'f':
        return (value - 32) * 5/9
    elif to_unit == 'k':
        return value - 273

# перевод всех единиц из цельсии
def from_c(value, to_unit):
    if to_unit == 'c':
        return value
    elif to_unit == 'f':
        return (value * 9/5)  + 32
    elif to_unit == 'k':
        return value + 273