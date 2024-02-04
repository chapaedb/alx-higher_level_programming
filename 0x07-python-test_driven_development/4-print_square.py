#!/usr/bin/python3

def print_square(size):
    """ Makes square with the character"""
    if not isinstance(size, int):
        raise TypeEror("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")
    print('#' * 3)
