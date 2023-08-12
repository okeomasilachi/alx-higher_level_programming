#!/usr/bin/python3
import calculator_1
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] in "+-*/":
            a = int(argv[1])
            b = int(argv[3])
            match (argv[2]):
                case '+':
                    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
                case '-':
                    print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
                case '*':
                    print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
                case '/':
                    print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
