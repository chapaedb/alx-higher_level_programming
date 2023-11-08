#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj (object): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add a new attribute to the object.")
    setattr(obj, att, value)
