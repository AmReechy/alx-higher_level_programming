#!/usr/bin/python3
"""

This module contain a function that prints a square
This is done by using the character # for the printing.

"""


def print_square(size):
    """This function prints a square with the character #

    Args:
        size (int): length of the square

    Raises:
        TypeError: If size not an int
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero

    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
