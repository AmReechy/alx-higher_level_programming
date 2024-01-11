#!/usr/bin/python3
"""Module with function that checks if
an object is a subclass of a specified class"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass
    of a_class, False otherwise
    """
    return issubclass(type(obj),a_class) and (type(obj) != a_class)
