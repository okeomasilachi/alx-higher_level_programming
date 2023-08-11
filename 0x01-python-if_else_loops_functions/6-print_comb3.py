#!/usr/bin/python3
def print_two_digits(i, j):
    if i < j:
        print("{}{}".format(i, j), end="\n" if i == 8 and j == 9 else ", ")


for i in range(10):
    for j in range(i + 1, 10):
        print_two_digits(i, j)

