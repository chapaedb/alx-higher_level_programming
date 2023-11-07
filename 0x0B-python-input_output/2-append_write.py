#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    If the file doesn’t exist, it will be created.

    Args:
        filename (str): The name of the file.
        text (str): The string to append.

    Returns:
        int: The number of characters added to the file.
    """
    count = 0
    with open(filename, "a", encoding="utf-8") as file:
        count = file.write(text)
    return count
