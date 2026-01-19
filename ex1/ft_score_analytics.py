import sys


def get_average(scores: list) -> float:
    """Calculates the average of a list of scores."""
    total = sum(scores)
    return (total / len(scores))


def ft_score_analytics():
    """Analyzes player scores provided as command-line arguments."""

    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return

    scores: list[int] = []
    for i in range(1, len(sys.argv)):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError as e:
            print(f"Error: One of your score is not an integer:\n{e}\n")
            return

    print(f"Scores processed:{scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {get_average(scores)}")
    print(f"The best: {max(scores)}")
    print(f"The worst: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    ft_score_analytics()
