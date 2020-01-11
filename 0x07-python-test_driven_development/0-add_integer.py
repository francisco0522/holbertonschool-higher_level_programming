#!/usr/bin/python3
"""
Write a function that adds 2 integers. For example,
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """
    Return the add of 2 integers.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    c = a + b
    return c
