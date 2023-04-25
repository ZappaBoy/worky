import os


def file_type(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)
