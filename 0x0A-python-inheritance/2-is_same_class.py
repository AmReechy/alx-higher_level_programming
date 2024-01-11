#!/usr/bin/python3
"""
Module to check if an object belongs to a class
"""


def is_same_class(obj, a_class):
    """This function if the given obj is an instance
    of the specified a_class
    
    Args:
        obj: any python object
        a_class: a python class
        
    Return:
        True or False (Boolean)
    """
    return (type(obj) == a_class)
