#!/usr/bin/python3
"""Defines a square."""


class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
