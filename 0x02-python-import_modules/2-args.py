#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if (len(argv) - 1) == 0:
        print("{} arguments.".format(len(argv) - 1))
    else:
        print("{} argument".format(len(argv) - 1),
              end=":\n" if (len(argv) - 1) == 1 else "s:\n")
    if (len(argv) - 1) > 0:
        for i in range(1, (len(argv))):
            print("{}: {}".format(i, argv[i]))
