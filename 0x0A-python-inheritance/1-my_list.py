#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    Implements sorted printing for the built-in list class.

    Attributes:
        Inherits all attributes from the built-in list class.
    """

    def print_sorted(self):
        """
        Print a list in sorted ascending order.

        Args:
            self: The MyList object to print.
        """
        print(sorted(self))
