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
        current_value = symbol_values[roman_string[i]]
        next_value = symbol_values[roman_string[i + 1]] if i + 1 < len(roman_string) else 0

        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    return result
