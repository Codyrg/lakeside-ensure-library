def ensure_positive(value):
    if value <= 0:
        raise ValueError("Value must be positive.")


def ensure_negative(value):
    if value >= 0:
        raise ValueError("Value must be negative.")


def ensure_non_zero(value):
    if value == 0:
        raise ValueError("Value must not be zero.")


def ensure_divisible_by(value, divisor):
    if value % divisor != 0:
        raise ValueError(f"Value must be divisible by {divisor}.")


def ensure_not_divisible_by(value, divisor):
    if value % divisor == 0:
        raise ValueError(f"Value must not be divisible by {divisor}.")


def ensure_positive_or_zero(value):
    if value < 0:
        raise ValueError("Value must be positive or zero.")


def ensure_negative_or_zero(value):
    if value > 0:
        raise ValueError("Value must be negative or zero.")


def ensure_in_range(value, lower_bound, upper_bound):
    if not lower_bound <= value <= upper_bound:
        raise ValueError(f"Value must be within range {lower_bound} and {upper_bound}.")


def ensure_multiple_of(value, multiple):
    if value % multiple != 0:
        raise ValueError(f"Value must be a multiple of {multiple}.")


def ensure_not_multiple_of(value, multiple):
    if value % multiple == 0:
        raise ValueError(f"Value must not be a multiple of {multiple}.")
