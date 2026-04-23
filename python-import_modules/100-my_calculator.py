#!/usr/bin/python3
"""Calculator program"""
import sys
import calculator_1 as calc

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    ops = {"+": calc.add, "-": calc.sub, "*": calc.mul, "/": calc.div}

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))