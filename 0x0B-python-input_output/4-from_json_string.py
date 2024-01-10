#!/usr/bin/python3
"""
This program converts json string
to a python object
"""


import json


def from_json_string(my_str):
    """
    Returns a python object represented by a JSON string
    Args:
      - my_str: str
    """
    return (json.loads(my_str))
