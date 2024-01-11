#!/usr/bin/python3
"""Module containig a rebel int class"""


class MyInt(int):
    """A rebel integer class that subclasses normal
    python int class.
    == and != comparison operators for this class are
    opposite of their normal behaviour"""
    def __eq__(self, other):
        """Custom method for equality check"""
        if isinstance(other, (int,MyInt)):
            return self.real != other.real

    def __ne__(self, other):
        """Custom method for inequality check"""
        if isinstance(other, (int,MyInt)):
            return self.real == other.real
