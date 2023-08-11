#!/usr/bin/python3
for pos in range(97, 123):
    if pos == 101 or pos == 106:
        continue
    print("{0}".format(chr(pos)), end="")
