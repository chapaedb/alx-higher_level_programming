#!/usr/bin/python3

"""Defines a class Student."""


class Student:
    """Represent a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student. 
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        """Get a dictionary representation of the Student.       
        If attributes is a list of strings, represent only those attributes
        included in the list.        
        Args:
            attributes (list): (Optional) The attributes to represent.        
        Returns:
            dict: The dictionary representation of the Student object.
        """
        if (type(attributes) == list and
                all(type(element) == str for element in attributes)):
            return {k: getattr(self, k) for k in attributes if hasattr(self, k)}
        return self.__dict__
