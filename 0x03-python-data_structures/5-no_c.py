#!/usr/bin/python3
def no_c(my_string):
    mystr = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        else:
            mystr += x
    return mystr
