#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

print("{} + {} = {}".format(a, op, b, add(a, b)))
print("{} - {} = {}".format(a, op, b, sub(a, b)))
print("{} * {} = {}".format(a, op, b, mul(a, b)))
print("{} / {} = {}".format(a, op, b, div(a, b)))
