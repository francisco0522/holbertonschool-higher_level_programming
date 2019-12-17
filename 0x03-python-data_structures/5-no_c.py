#!/usr/bin/python3
def no_c(my_string):
    copy = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'C' and my_string[i] != 'c':
            copy += my_string[i]
    return copy
