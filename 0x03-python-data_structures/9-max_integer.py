#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        list = sorted(my_list)
        return (list[len(list) - 1])
