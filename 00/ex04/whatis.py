#!/usr/bin/env python3

import sys


def get_args() -> list:
    return sys.argv[1:]


args = get_args()
if len(args) == 0:
    print("AssertionError: no arguments provided.")
    sys.exit(1)
elif len(args) > 1:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)
try:
    int(args[0])
except ValueError:
    print("AssertionError: argument is not an integer")
print("I'm ", end="")
print("Even." if int(args[0]) % 2 == 0 else "Odd.")
