#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] in "+-*/":
            a = int(argv[1])
            b = int(argv[3])
            match argv[2]:
                case '+':
                    print("{} + {} = {}".format(a, b, add(a, b)))
                case '-':
                    print("{} - {} = {}".format(a, b, sub(a, b)))
                case '*':
                    print("{} * {} = {}".format(a, b, mul(a, b)))
                case '/':
                    print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
