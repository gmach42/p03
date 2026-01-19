# len(), print(), sum(), max(), min(), sorted()


class AnalyticsDashboard:
    """Class for analytics dashboard methods"""

    class Lists:
        """Class for list comprehension methods"""

        @staticmethod
        def repeatead_digits(nb: int) -> bool:
            """Check if a number has repeated digits"""
            digits = str(nb)
            return len(digits) != len(set(digits))

        @staticmethod
        def list_analytics(content: dict) -> None:
            """Perform list comprehension analytics on game data"""
            high_scorers = [
                name
                for name, data in content["players"].items()
                if data["total_score"] > 2000
            ]
            # return scores with doubled digits
            scores_reapeated_digits = [
                player["score"]
                for player in content["sessions"]
                if AnalyticsDashboard.Lists.repeatead_digits(player["score"])
            ]
            active_players = [
                session["player"]
                for session in content["sessions"]
                if session["completed"] is True
            ]
            print(f"High scorers: {high_scorers}")
            print(f"Scores with repeated digits: {scores_reapeated_digits}")
            print(f"Active players: {active_players}\n")

    class Dictionaries:
        """Class for dictionary comprehension methods"""

        @staticmethod
        def dict_analytics(content: dict) -> None:
            """Perform dictionary comprehension analytics on game data"""
            player_scores = {
                player["player"]: player["score"]
                for player in content["sessions"]
            }
            score_categories = {
                player["player"]: ("High" if player["score"] > 2000 else "Low")
                for player in content["sessions"]
            }
            achievement_counts = {
                name: data["achievements_count"]
                for name, data in content["players"].items()
            }
            print(f"Player Scores: {player_scores}")
            print(f"Score Categories: {score_categories}")
            print(f"Achievement Counts: {achievement_counts}\n")

    class Sets:
        """Class for set comprehension methods"""

        @staticmethod
        def set_analytics(content: dict) -> None:
            """Perform set comprehension analytics on game data"""
            unique_players = {
                session["player"] for session in content["sessions"]
            }
            unique_achievements = set(content["achievements"])
            unique_modes = set(content["game_modes"])
            duplicated_scores = {
                score
                for score in [
                    data["total_score"] for data in content["players"].values()
                ]
                if [
                    data["total_score"] for data in content["players"].values()
                ].count(score)
                >= 2
            }
            print(f"Unique Players: {unique_players}")
            print(f"Unique Achievements: {unique_achievements}")
            print(f"Unique Modes: {unique_modes}")
            print(f"Duplicated Scores: {duplicated_scores}\n")

    class Analytics:
        """Class for combined analytics methods"""

        @staticmethod
        def combined_analytics(content: dict) -> None:
            """Perform combined analytics on game data"""
            total_players = len(content["players"])
            total_unique_achievements = len(
                {achiev for achiev in content["achievements"]}
            )
            average_score = sum(
                player["score"] for player in content["sessions"]
            ) / len(content["sessions"])
            top_performer = max(
                content["players"].items(), key=lambda x: x[1]["total_score"]
            )[0]
            print(f"Total Players: {total_players}")
            print(f"Total Unique Achievements: {total_unique_achievements}")
            print(f"Average Score: {average_score:.2f}")
            print(f"Top Performer: {top_performer}\n")


def main():
    print("=== Game Analytics Dashboard ===\n")

    try:
        # Using eval() here to transform the string into a readable list
        with open("data.txt", "r") as file:
            content = eval(file.read())
        # print(content)
        print("=== List Comprehension Examples ===")
        AnalyticsDashboard.Lists.list_analytics(content)

        print("=== Dictionary Comprehension Examples ===")
        AnalyticsDashboard.Dictionaries.dict_analytics(content)

        print("=== Set Comprehension Examples ===")
        AnalyticsDashboard.Sets.set_analytics(content)

        print("=== Combined Analysis ===")
        AnalyticsDashboard.Analytics.combined_analytics(content)

    except FileNotFoundError:
        print("Please add a data.txt file to run the analytics dashboard :)")
    except TypeError:
        print(
            "Please verify that the events are correctly "
            "implemented in your data.txt file"
        )


if __name__ == "__main__":
    main()
