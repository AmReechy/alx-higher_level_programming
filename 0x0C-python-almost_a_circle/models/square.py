#!/usr/bin/python3
"""This module defines model class for
creating square objects. The class inherits from rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Model class for square objects"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size of a square object"""
        return self.__width

    @size.setter
    def size(self, value):
        """Assigns value to the size of a square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
            
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of a square instance"""

        if args is not None and not args:
            l = len(args)
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if l > 1:
                self.size = args[1]
            if l > 2:
                self.x = args[2]
            if l > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary representing a square object"""

        square_dict = {'id': self.id, 
                       'size': self.size, 
                       'x': self.x,
                       'y': self.y}

        return square_dict

    def __str__(self):
        """returns a nicely formatted string representation
        of a square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        
