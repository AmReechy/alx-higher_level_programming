#!/usr/bin/python3
"""
Module with a Rectangle class that subclasses
Basegeometry Class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeomety

class Rectangle(BaseGeometry):
    """This is a Rectangle class which subclasses
    BaseGeometry class"""
    def __init__(self, width, height):
        """Initialization method for the Rectangle class"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
