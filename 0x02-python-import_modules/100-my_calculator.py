#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        c = add(a, b)
        d = sub(a, b)
        e = mul(a, b)
        f = div(a, b)
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, c))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, d))
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, e))
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(a, b, c))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
