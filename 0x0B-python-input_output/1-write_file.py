#!/usr/bin/python3
"""
This simple program writes into a file the
contents of a given text
"""


def write_file(filename="", text=""):
    """
    Writes the value of text into a file given by filename.
    if filename doesn't exist, it is created
    if filename exists, it is overwritten
    
    Args:
      - filename: string- the file to be written to
      - text: string - the text to be written to the file
    """

    with open(filename, mode="w", encoding="utf-8") as _f:
        chars_written = _f.write(text)

    return chars_written
