#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
    return func
