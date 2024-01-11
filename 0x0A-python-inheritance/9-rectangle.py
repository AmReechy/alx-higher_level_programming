#!/usr/bin/python3
"""
Module with a Rectangle class that subclasses
Basegeometry Class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """This is a Rectangle class which subclasses
    BaseGeometry class"""
    
    def __init__(self, width, height):
        """Initialization method for the Rectangle class"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implementation of the area of the Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Method that return a string representation of the object"""
        return f"[Rectangle] {width}/{height}"
