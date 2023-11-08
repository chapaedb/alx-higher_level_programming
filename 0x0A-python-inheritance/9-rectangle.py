#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry.

    This class inherits from the BaseGeometry class.
    """

    def __init__(self, width: int, height: int):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """
        Return the string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
