#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    if len(sys.argv) == 1:
        print("0")
    else:
        for i in range(1, len(sys.argv)):
            result = result + int(sys.argv[i])
        print("{:d}".format(result))
