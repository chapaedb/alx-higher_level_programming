#!/usr/bin/python3
def add_integer(a, b = 98):
    """Adds two integers 
    Args:
        a (int): First integer
        b (int, optional) : second integer"""
    if not isinstance(a, (int , float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")
    return int(a) +int(b)
