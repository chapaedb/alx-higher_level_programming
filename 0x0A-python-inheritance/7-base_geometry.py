#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    Represents the base geometry.

    This class serves as a base for other geometry classes.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        This method is not implemented in the base class.

        Raises:
            Exception: If the area() method is called on the base class.

        Returns:
            None.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, param_name, param_value):
        """
        Validate a parameter as an integer.

        Args:
            param_name (str): The name of the parameter.
            param_value (int): The parameter to validate.

        Raises:
            TypeError: If param_value is not an integer.
            ValueError: If param_value is less than or equal to 0.
        """
        if type(param_value) != int:
            raise TypeError("{} must be an integer".format(param_name))
        if param_value <= 0:
            raise ValueError("{} must be greater than 0".format(param_name))
