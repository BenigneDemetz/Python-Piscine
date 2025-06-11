#!/usr/bin/env python3

import sys


def get_args() -> list:
    """Get command line arguments."""
    return sys.argv[1:]


def get_string() -> str:
    """Get a string from command line arguments or prompt."""

    args = get_args()
    if len(args) == 0:
        print("Please provide a string:")
        input_string = sys.stdin.readline()
        if input_string[-1:] != '\n':
            print()
    elif len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return None
    else:
        input_string = args[0]
    return str(input_string)


def count_characters(string: str) -> int:
    """Count the number of characters in a string."""
    return len(string)


def count_uppercase(string: str) -> int:
    """Count the number of uppercase characters in a string."""
    return sum(1 for char in string if char.isupper())


def count_lowercase(string: str) -> int:
    """Count the number of lowercase characters in a string."""
    return sum(1 for char in string if char.islower())


def count_punctuation(string: str) -> int:
    """Count the number of punctuation characters in a string."""
    ponctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return sum(1 for char in string if char in ponctuation)


def count_spaces(string: str) -> int:
    """Count the number of space characters in a string."""
    return sum(1 for char in string if char.isspace() or char == '\n')


def count_digits(string: str) -> int:
    """Count the number of digit characters in a string."""
    return sum(1 for char in string if char.isdigit())


def main():
    """Main function to execute the script."""
    string = get_string()
    if string is None:
        return
    print(f"The text contains {count_characters(string)} characters:")
    print(f"{count_uppercase(string)} uppercase letters")
    print(f"{count_lowercase(string)} lowercase letters")
    print(f"{count_punctuation(string)} punctuation marks")
    print(f"{count_spaces(string)} spaces")
    print(f"{count_digits(string)} digits")


if __name__ == "__main__":
    # main()
    print(count_characters.__doc__)
