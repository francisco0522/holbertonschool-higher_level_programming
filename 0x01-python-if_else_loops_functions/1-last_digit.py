#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = "Last digit of"
less = "less than 6 and not 0"
if number < 0:
    number1 = number * -1
else:
    number1 = number
last = number1 % 10
if last > 5:
    print("{} {:d} is {:d} and is greater than 5".format(l, number, last))
elif last == 0:
    print("{} {:d} is {:d} and is 0".format(l, number, last))
else:
    print("{} {:d} is {:d} and is {}".format(l, number, last, less))
