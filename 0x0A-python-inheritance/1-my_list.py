#!/usr/bin/python3
"""
This module consists of a class, Mylist, that is a child
of the normal list class
"""


class Mylist(list):
    """This is a child class of list class
    The class implements a method that prints the sorted
    form of the list
    """
    def print_sorted(self):
        """This method prints the ascendingly sorted list object
        """
        self.sort()
        print(self)
        
