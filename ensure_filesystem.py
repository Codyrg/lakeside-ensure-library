import os


def ensure_file_exists(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File {filepath} does not exist.")


def ensure_directory_exists(directory):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist.")


def ensure_has_permissions(filepath, permissions):
    if not os.access(filepath, permissions):
        raise PermissionError(f"File {filepath} does not have the necessary permissions.")


def ensure_file_extension(filepath, extension):
    _, ext = os.path.splitext(filepath)
    if ext.lower() != extension.lower():
        raise ValueError(f"File {filepath} must have extension {extension}.")
