# len(), print(), sum(), max(), min(), sorted()


def main():
    print("=== Game Analytics Dashboard ===\n")

    try:
        print("=== List Comprehension Examples ===")
        # Using eval() here to transform the string into a readable list
        with open("data.txt", "r") as file:
            content = eval(file.read())

        print(f"Data loaded: {content}\n")

        high_scorers = [player for player in content if player["score"] > 2000]
        doubled_scores = [player["score"] * 2 for player in content]
        active_players = [
            player["player"] for player in content if player["active"] is True
        ]
        print(f"High scorers: {high_scorers}")
        print(f"Doubled scores: {doubled_scores}")
        print(f"Active players: {active_players}\n")

        player_scores = {
            player["player"]: player["score"] for player in content
        }
        score_categories = {
            player["player"]: ("High" if player["score"] > 2000 else "Low")
            for player in content
        }
        achievement_counts = {
            player["player"]: len(player["achievements"]) for player in content
        }
        print(f"Player Scores: {player_scores}")
        print(f"Score Categories: {score_categories}")
        print(f"Achievement Counts: {achievement_counts}\n")

        print("=== Set Comprehension Examples ===")
        unique_players = {player["player"] for player in content}
        unique_achievements = {
            achievement
            for player in content
            for achievement in player["achievements"]
        }
        active_regions = {
            player["region"] for player in content if player["active"] is True
        }
        print(f"Unique Players: {unique_players}")
        print(f"Unique Achievements: {unique_achievements}")
        print(f"Active Regions: {active_regions}\n")

        print("=== Combined Analysis ===")
        total_players = len(content)
        total_unique_achievements = len(unique_achievements)
        average_score = (
            sum(player["score"] for player in content) / total_players
        )
        top_performer = max(content, key=lambda player: player["score"])[
            "player"
        ]
        print(f"Total Players: {total_players}")
        print(f"Total Unique Achievements: {total_unique_achievements}")
        print(f"Average Score: {average_score}")
        print(f"Top Performer: {top_performer}\n")

    except FileNotFoundError:
        print("Please add a data.txt file")
    except TypeError:
        print(
            "Please verify that the events are correctly "
            "implemented in your data.txt file"
        )


if __name__ == "__main__":
    main()
