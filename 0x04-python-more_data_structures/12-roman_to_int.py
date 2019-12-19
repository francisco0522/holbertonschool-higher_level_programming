#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        num = [1, 5, 10, 50, 100, 500, 1000]
        roman = ["I", "V", "X", "L", "C", "D", "M"]
        result = 0
        for i in range(len(roman_string)):
            idx = roman.index(roman_string[i])
            result = result + num[idx]
        return result
    else:
        return 0
