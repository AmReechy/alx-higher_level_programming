#!/usr/bin/python3
"""Module containig a rebel int class"""


class MyInt(int):
    """A rebel integer class that subclasses normal
    python int class.
    == and != comparison operators for this class are
    opposite of their normal behaviour"""
    def __eq__(self, other):
        """Custom method for equality check"""
        return self != other

    def __ne__(self, other):
        """Custom method for inequality check"""
        return self == other
