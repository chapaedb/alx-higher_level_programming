#!/usr/bin/python3

def custom_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        result = add(a, b)
        for i in range(4, 6):
            result = add(result, i)
        return result

    else:
        return sub(a, b)
