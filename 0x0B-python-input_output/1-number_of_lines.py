#!/usr/bin/python3
def number_of_lines(filename=""):
    count = 0
    for line in open(filename):
        count += 1
    return (count)
