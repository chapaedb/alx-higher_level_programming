#!/usr/bin/python3
a = 1
b = 2
from add_0 import add

result = add(a, b)
print("{} + {} = {}".format(a, b, result))
=======
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)
