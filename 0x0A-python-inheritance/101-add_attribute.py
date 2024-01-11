#!/usr/bin/python
"""MOdule with a function to add attribute to an object"""


def add_attribute(obj, attr, value):
    """Add attribute to an object"""
    return setattr(obj, attr, value)
