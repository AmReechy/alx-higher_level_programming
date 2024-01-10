#!/usr/bin/python3
"""
The function in this module returns the list
of available attributes and methods of an object
"""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object
    
    Args:
        obj: any python object; an instance of a class

    Returns:
        List of attributes and methods of the object
    """
    return dir(obj)
