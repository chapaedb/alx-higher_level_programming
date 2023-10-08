#!/usr/bin/env python3
def no_c(my_string):
    mystr = ""
    for x in my_string:
        if x.lower() != 'c':
            mystr += x
    return mystr
