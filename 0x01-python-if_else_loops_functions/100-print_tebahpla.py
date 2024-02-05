#!/usr/bin/python3

def print_reversed_alphabet():
    for ascii_val in range(122, 64, -1):
        char = chr(ascii_val)
        case = 'lower' if ascii_val % 2 == 0 else 'upper'
        print(char.upper() if case == 'upper' else char, end='')
