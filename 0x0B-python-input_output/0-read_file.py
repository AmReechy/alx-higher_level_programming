#!/usr/bin/python3
"""
This module contains a function that reads files
"""


def read_file(filename=""):
    """
    This function reads a file and prints it's content
    to the standard output
    """

    with open(filename, encoding="utf-8") as _f:
        print(_f.read())
