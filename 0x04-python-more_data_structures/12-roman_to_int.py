#!/usr/bin/python3
def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    symbol_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and symbol_values[roman_string[i]] < symbol_values[roman_string[i + 1]]:
            result -= symbol_values[roman_string[i]]
        else:
            result += symbol_values[roman_string[i]]

    return result
