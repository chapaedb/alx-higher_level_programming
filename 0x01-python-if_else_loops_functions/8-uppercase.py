#!/usr/bin/python3
def uppercase(string):
    for char in string:
        val = ord(char)
        if val >= 97 and val <= 122:
            ascii_val = val - 32
        print("{}".fotmat(chr(ascii_val)), end = "")
    
