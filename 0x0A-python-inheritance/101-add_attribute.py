#!/usr/bin/python
"""MOdule with a function to add attribute to an object"""


def add_attribute(obj, attr, value):
    """Add attribute to an object"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
