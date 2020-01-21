#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    count = 0
    for line in open(filename): count += 1
    with open(filename) as file:
        if nb_lines <= 0 or nb_lines >= count:
            data = file.read()
            print(data)
        i = 0
        line = file.readline()
        while i < nb_lines:
            print(line)
            line = file.readline()
            i += 1


