#!/usr/bin/python3
"""
This program writes a python Object to a text file,
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Save in a file data with JSON format,
    if the files doesn't exist, it is created.
    Args:
      - my_obj: python object to be json serialized
      - filename: str (file path to be written to)
    """

    with open(filename, mode="w", encoding="utf-8") as _file:
        _file.write(json.dumps(my_obj))
