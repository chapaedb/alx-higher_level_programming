#!/usr/bin/python3
"""Defines a square."""


class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the.
        """
        return self.__size ** 2
~
