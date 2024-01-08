#!/usr/bin/python3
"""
This module contains a single function matrix_divided
that does some matrix division
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists 
        div: Number to be used for the division 
    Raises:
        TypeError: If the matrix contains non-numeric values
        TypeError: If the matrix contains rows of that are not equal in sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
        All values in matrix have been divided by div, rounded to 2 decimal places
    """
    if (not isinstance(matrix, list) or matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
        if not len(row) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
