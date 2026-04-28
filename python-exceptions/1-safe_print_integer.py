#!/usr/bin/python3
def safe_print_integer(value):
    print("{:d}".format(value))
    try:
        return True
    except ValueError:
        return False
