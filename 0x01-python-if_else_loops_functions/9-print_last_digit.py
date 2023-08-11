#!/usr/bin/python3
# prints the last digit of a givien number
def print_last_digit(number):
    val = str(number)[-1]
    val = int(val)
    print(f"{val}", end="")
    return val
