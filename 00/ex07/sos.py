#!/usr/bin/env python3

from benigne.get_args import get_args
from benigne.ft_filter import ft_filter

NESTED_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': '/', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}


def main():
    args: list[str] = get_args()
    if len(args) != 1 or not args[0].replace(" ", "").isalnum():
        print("AssertionError: the arguments are bad")
        return
    string = args[0].upper()
    ft_filter(lambda c: print(NESTED_MORSE[c], end=' '), string)
    print()

if __name__ == "__main__":
    main()