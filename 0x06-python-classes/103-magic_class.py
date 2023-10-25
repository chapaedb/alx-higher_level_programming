#!/usr/bin/python3

"""
MagicClass module
"""

import math


class MagicClass:
    """
    A class representing a Magic Circle
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a given radius.

        Args:
            radius (int or float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If the radius is not a number.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
