#!/usr/bin/python3
"""This is a Geometry Module"""


class BaseGeometry:
    """This is an empty geometry class"""
    def area(self):
        """This method is not implemented for this class yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value argument"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
