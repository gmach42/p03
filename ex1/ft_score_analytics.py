#!/usr/bin/env python3

import sys


def get_average(scores: list):
    total = sum(scores)
    return (total / len(scores))


def main():

    print("=== Player Score Analytics ===\n")
    if len(sys.argv) < 2:
        print("Please enter a score to register")
        return

    scores: list[int] = []
    for i in range(1, len(sys.argv)):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError as e:
            print(f"One of your score is not an integer:\n{e}\n")
            return

    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {get_average(scores)}")
    print(f"The best: {max(scores)}")
    print(f"The worst: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    print(f"Scores recap:\n{scores}")


if __name__ == "__main__":
    main()
