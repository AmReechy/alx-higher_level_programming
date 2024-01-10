#!/usr/bin/python3
"""
This program appends a given text to a file,
The file is created if it doesn't already exist
"""


def append_write(filename="", text=""):
    """
    This function appends the fiven text to the end of the given filename
    The filename is created if it doesn't exist
    Args:
      - filename: string (path of file to be appended to)
      - text: string (text string to be appended to the file)
    """

    with open(filename, mode="a", encoding="utf-8") as _file:
        chars_written = _file.write(text)

    return chars_written
