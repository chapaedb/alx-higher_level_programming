#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file.

    This function reads the contents of the specified file, searches for lines
    that contain the provided search string, and inserts the specified new
    string after each matching line. The modified text is then written back to
    the same file, overwriting its previous contents.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after each line containing the
            search string.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
