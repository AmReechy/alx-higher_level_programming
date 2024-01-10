#!/usr/bin/python3
"""
This module contaains a function that returns 
the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    Args:
     - my_obj: python object to be json serialized
    """

    return (json.dumps(my_obj))
