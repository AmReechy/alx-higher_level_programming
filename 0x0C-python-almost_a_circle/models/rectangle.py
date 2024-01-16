#!/usr/bin/python3
"""This module defines a rectangle model class"""

from models.base import Base


class Rectangle(Base):
    """Model class for creating rectangles"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes for a rectangle object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """returns the value for height"""
        return self.__height

    @property
    def width(self):
        """returns the value for width"""
        return self.__width

    @property
    def y(self):
        """returns the value for y"""
        return self.__y

    @property
    def x(self):
        """returns the value for x"""
        return self.__x

    # List of setter functions
    @width.setter
    def width(self, value):
        """Sets the value of the width attribute for the object"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value of the height attribute for the object"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the value for x for s rectangle object"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the value for y for s rectangle object"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """computes and returns the area of the rectangle object"""
        return (self.__height * self.__width)

    def display(self):
        """Displays the rectangle using the character '#' """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """returns a nicely formatted string representation
        of a rectangle object"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if args:
            for a, arg in enumerate(args):
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns a dictionary representing a Rectangle object"""

        return {'id': self.id, 
                'width': self.__width, 
                'height': self.__height, 
                'x': self.__x,
                'y': self.__y}

