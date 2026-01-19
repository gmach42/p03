#!/usr/bin/env python3

import sys


def ft_command_quest():
    """Displays the arguments passed to the script."""

    print("=== Command Quest ===")
    nb_args = len(sys.argv) - 1

    # Handle no arguments case
    if nb_args == 0:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")

    # Handle arguments case
    if nb_args != 0:
        print(f"Arguments received: {nb_args}")
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    ft_command_quest()
