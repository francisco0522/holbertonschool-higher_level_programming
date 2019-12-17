#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for i in my_list:
        if i % 2 == 0:
            list.apend(True)
        else:
            list.apend(False)
    return list
