#!/usr/bin/python3
a = 1
b = 2
from add_0 import add

result = add(a, b)
print("{} + {} = {}".format(a, b, result))
=======
from add_0 import add

a = 1
b = 2

print("{} + {} = {}".format(a, b, add(a, b)))
