#!/usr/bin/python3
def uppercase(string):
    for char in string:
        val = ord(char)
        if val >= 97 and val <= 122:
            ascii_val -= 32
        print(chr(val), end="")
    print()
