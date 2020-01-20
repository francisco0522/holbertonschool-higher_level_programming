#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """that prints the list, but sorted"""
    def print_sorted(self):
        print(sorted(self))
