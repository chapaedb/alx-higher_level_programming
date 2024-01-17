#!/usr/bin/python3

def print_last_digit(number):
    my_list = str(number)
    length = len(my_list)
    print("{}".format(my_list[length - 1]), end="")
    return my_list[length - 1]
