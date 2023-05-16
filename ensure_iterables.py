def ensure_non_empty(value):
    if not value:
        raise ValueError("Value must not be empty.")


def ensure_length(value, length):
    if len(value) != length:
        raise ValueError(f"Value must have length {length}.")


def ensure_min_length(value, min_length):
    if len(value) < min_length:
        raise ValueError(f"Value must have a minimum length of {min_length}.")


def ensure_max_length(value, max_length):
    if len(value) > max_length:
        raise ValueError(f"Value must have a maximum length of {max_length}.")


def ensure_length_within_range(value, min_length, max_length):
    if not min_length <= len(value) <= max_length:
        raise ValueError(f"Value length must be within range {min_length} and {max_length}.")


def ensure_contains(value, element):
    if element not in value:
        raise ValueError(f"Value must contain element {element}.")


def ensure_same_length(iterable1, iterable2):
    if len(iterable1) != len(iterable2):
        raise ValueError("Both iterables must have the same length.")


def ensure_unique_elements(iterable):
    if len(iterable) != len(set(iterable)):
        raise ValueError("Iterable must contain unique elements.")


def ensure_contains_only(iterable, allowed_values):
    if not set(iterable).issubset(allowed_values):
        raise ValueError("Iterable must only contain allowed values.")


def ensure_iterable_not_empty(iterable):
    if not iterable:
        raise ValueError("Iterable must not be empty.")
