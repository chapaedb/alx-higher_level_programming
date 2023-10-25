#!/usr/bin/python3

"""
Module: magic_class.py
This module defines the MagicClass that performs calculations related to circles.
"""

import math


class MagicClass:
    """
    MagicClass represents a circle and provides methods to calculate its area and circumference.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass object with the given radius.

        Args:
            radius (float): The radius of the circle. Default is 0.
        
        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
