#!/usr/bin/python3

"""
Square module
"""


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Args:
            size (int or float): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal in area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal in area, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compares two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square has a greater area than the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square has a greater or equal area to the other square, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compares two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square has a smaller area than the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square has a smaller or equal area to the other square, False otherwise.
        """
        return self.area() <= other.area()
