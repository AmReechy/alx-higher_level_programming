#!/usr/bin/python3
"""
This program define a Student in a class
and serializes all its public attributes
"""


class Student():
    """
    Class of a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialization method of the class
        Args:
          - first_name: str
          - last_name: str
          - age: int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return the dict representation of the instance
        """
        return (self.__dict__)
