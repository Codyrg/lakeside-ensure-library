def ensure_key_exists(dictionary, key):
    if key not in dictionary:
        raise KeyError(f"Key {key} does not exist in the dictionary.")


def ensure_value_exists(dictionary, value):
    if value not in dictionary.values():
        raise ValueError(f"Value {value} does not exist in the dictionary.")
