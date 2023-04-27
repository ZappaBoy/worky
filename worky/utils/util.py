import os


def file_type(string):
    if os.path.isfile(string):
        return string


def dir_exists(dir_path: str):
    return os.path.isdir(dir_path)
