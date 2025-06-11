#!/usr/bin/env python3

import sys
import getopt

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:v", ["help", "age=", "verbose"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    
    verbose = False
    age = None
    print(opts, args)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Usage: script.py -a <age> -v")
            sys.exit()
        elif opt in ("-a", "--age"):
            age = int(arg)
        elif opt in ("-v", "--verbose"):
            verbose = True

if __name__ == "__main__":
    main()