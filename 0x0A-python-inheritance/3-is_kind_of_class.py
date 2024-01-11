#!/usr/bin/python3
"""
Module with a function that checks if a given object
is an instance of a specified class or an instance of a
subclass of the specified class
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class
    or an instance of a subclass of a_class
    It returns True or False accordingly"""
    return isinstance(obj, a_class)
