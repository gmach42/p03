#!/usr/bin/env python3

import sys


def main():
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")

    nb_args = len(sys.argv) - 1
    i = 1
    if nb_args != 0:
        print(f"Arguments received: {nb_args}")
    while i <= nb_args:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
