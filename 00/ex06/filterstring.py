#! /usr/bin/env python3

import sys
from benigne.get_args import get_args
from benigne.ft_filter import ft_filter


def main():
    """Main function to execute the script."""
    args: list[str] = get_args()
    if len(args) != 2 or not args[1].isdigit():
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    words = args[0].split(' ')
    print(list(ft_filter(lambda W: len(W) >= int(args[1]), words)))


if __name__ == "__main__":
    main()
