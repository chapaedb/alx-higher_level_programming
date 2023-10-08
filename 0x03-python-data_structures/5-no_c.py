#!/usr/bin/env python3
def no_c(my_string):
    mystr = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            mystr += x
    return mystr
