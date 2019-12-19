#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        num = [1, 5, 10, 50, 100, 500, 1000]
        roman = ["I", "V", "X", "L", "C", "D", "M"]
        result = 0
        prev = 1001
        for i in range(len(roman_string)):
            idx = roman.index(roman_string[i])
            if prev >= num[idx]:
                result = result + num[idx]
                prev = num[idx]
            else:
                result = num[idx] - 2 * prev + result
                prev = num[idx]
        return result
    else:
        return 0
