#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
from typing import Union
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.

    This class inherits from the Rectangle class.
    """

    def __init__(self, size: Union[int, float]):
        """
        Initialize a new square.

        Args:
            size (Union[int, float]): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
