#!/usr/bin/python3
if __name__ == "__main__":
    import sys
arguments = len(sys.argv) - 1
print("{} arguments".format(arguments))
for i in range(1, arguments + 1):
    argum = sys.argv[i]
    print ("{}: {}".format(i,argum))
