#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    Represents a custom integer class with inverted equality operators.

    This class inherits from the int class.
    """

    def __eq__(self, value):
        """
        Override the == operator with != behavior.

        Args:
            value: The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override the != operator with == behavior.

        Args:
            value: The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.real == value
