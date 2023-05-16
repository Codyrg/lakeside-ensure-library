def ensure_not_none(value):
    if value is None:
        raise TypeError("None is not an acceptable value.")


def ensure_type(value, type_):
    if not isinstance(value, type_):
        raise TypeError(f"Expected value of type {type_}, got {type(value)}.")


def ensure_iterable(value):
    try:
        iter(value)
    except TypeError:
        raise TypeError(f"Value {value} is not iterable.")


def ensure_callable(value):
    if not callable(value):
        raise TypeError(f"Value {value} is not callable.")


def ensure_has_attribute(value, attribute):
    if not hasattr(value, attribute):
        raise AttributeError(f"Value {value} does not have attribute {attribute}.")


def ensure_subclass_of(subclass, superclass):
    if not issubclass(subclass, superclass):
        raise TypeError(f"{subclass} is not a subclass of {superclass}.")


def ensure_has_methods(value, methods_list):
    for method in methods_list:
        if not hasattr(value, method):
            raise AttributeError(f"Value {value} does not have method {method}.")
