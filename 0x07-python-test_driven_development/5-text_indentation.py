#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the given text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    lines = []
    line = ''

    for char in text:
        line += char
        if char in punctuation:
            lines.append(line.strip())
            lines.append('')  # Add an empty line after the punctuation
            line = ''

    # Append the remaining line if it is not empty
    if line:
        lines.append(line.strip())

    # Print the formatted text
    for line in lines:
        print(line)
