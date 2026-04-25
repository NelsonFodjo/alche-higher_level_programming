#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    i = 0
    if not isinstance(roman_string, str):
        return None
    
    while (i < len(roman_string)):
        condi = roman[roman_string[i]] < roman[roman_string[i+1]]
        if i + 1 < len(roman_string) and condi:
            number = number + roman[roman_string[i+1]] - roman[roman_string[i]]
            i = i + 2
        else:
            number += roman[roman_string[i]]
            i = i + 1
    return number
