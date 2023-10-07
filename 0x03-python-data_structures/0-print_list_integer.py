#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for x in my_list:
        print("{}".format(x))

# Test example
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
