#!/usr/bin/python3
up = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - up)), end="")
    up = 32 if up == 0 else 0
