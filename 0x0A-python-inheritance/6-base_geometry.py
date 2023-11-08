#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    Represents base geometry.

    This class serves as a base for other geometry classes.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        This method is not implemented in the base class.

        Raises:
            Exception: If the area() method is called on the base class.

        Returns:
            None
        """
        raise Exception("area() is not implemented")
