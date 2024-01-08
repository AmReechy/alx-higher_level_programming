#!/usr/bin/python3
"""
This module contains a single function for computing the sum of
two numeric arguments (int or floats)
"""


def add_integer(a, b=98):
    """Returns the sum of two integers or floats as integers

    Args:
        a: first argument -> int or float
        b: second argument -> int or float

    Returns:
        Sum of the two arguments -> int

    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    a , b = int(a), int(b)
    return (a + b)
