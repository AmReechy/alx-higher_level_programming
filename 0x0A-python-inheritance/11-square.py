#!/usr/bin/python3
"""Module contain a square class that subclasses
Rectangle class"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """A Square class subclassing Rectangle class"""

    def __init__(self, size):
        """Instantiates the class"""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Computes and returns the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """returns string representation of Square object"""
        return f"[Square] {self.__size}/{self.__size}"
