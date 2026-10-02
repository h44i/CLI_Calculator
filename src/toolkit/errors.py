class ToolkitError(Exception):
    pass


class Empty_Expression_Error(ToolkitError):
    pass


class Invalid_Symbol_Error(ToolkitError):
    pass


class Invalid_Expression_Error(ToolkitError):
    pass


class Division_By_Zero_Error(ToolkitError):
    pass


class Unknown_Unit_Error(ToolkitError):
    pass


class Incompatible_Units_Error(ToolkitError):
    pass


class Invalid_Temperature_Error(ToolkitError):
    pass
