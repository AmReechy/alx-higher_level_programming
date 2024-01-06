#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization method for rectangle class
        Args:
            width: integer width value for a rectangle
            height: integer height value for a rectangle
        Raises:
            TypeError: if width or height is not integer
            ValueError: if value of width or height is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute of rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """sets height attribute of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """computes the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """computes the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns a nicely formatted human readable string representation"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            for j in range(self.width):
                string += '#'
            else:
                string += '\n'
        return string

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every object that is deleted"""
        print("Bye rectangle...")
