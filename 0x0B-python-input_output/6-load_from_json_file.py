#!/usr/bin/python3
"""
This module contains a single function
that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Reads a json text file and serialize it to a python object
    The python object serialized is returned
    Args:
      - filename: path
    """

    with open(filename, mode="r", encoding="utf-8") as _file:
        return (json.loads(_file.read()))
