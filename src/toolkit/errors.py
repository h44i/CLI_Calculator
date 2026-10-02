class ToolkitError(Exception):
    pass


class EmptyExpressionError(ToolkitError):
    pass


class InvalidSymbolError(ToolkitError):
    pass


class InvalidExpressionError(ToolkitError):
    pass


class DivisionByZeroError(ToolkitError):
    pass


class UnknownUnitError(ToolkitError):
    pass


class IncompatibleUnitsError(ToolkitError):
    pass


class InvalidTemperatureError(ToolkitError):
    pass
