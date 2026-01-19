#!/usr/bin/env python3

class AchievementTracker:
    """Class to track player achievements in a game"""
    players = []

    def __init__(self, name: str):
        self.name = name
        self.achievements = set()
        AchievementTracker.players.append(self)

    def unlock(self, new_achievement: str):
        self.achievements.add(new_achievement)

    def unlock_multiple(self, *new_achievements: tuple):
        for new_achievement in new_achievements:
            self.achievements.add(new_achievement)

    def get_achievements(self):
        return self.achievements

    @classmethod
    def get_players(cls):
        return cls.players

    @classmethod
    def get_players_count(cls):
        return f"Number of players: {len(cls.players)}"

    @classmethod
    def create_achievements_examples(cls):
        players = [cls(name) for name in ["Alice", "Bob", "Charlie"]]
        players[0].unlock_multiple(
            'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
        )
        players[1].unlock_multiple(
            'first_kill', 'level_10', 'boss_slayer', 'collector'
        )
        players[2].unlock_multiple(
            'level_10', 'treasure_hunter', 'boss_slayer',
            'speed_demon', 'perfectionist'
        )
        return players

    def __str__(self):
        return f"Player {self.name} achievements: {self.achievements}"

    class Analytics:
        """Class for achievement analytics methods"""

        @staticmethod
        def get_all_unique(players):
            """Get all unique achievements across all players"""
            all_achievements = [
                player.get_achievements() for player in players
            ]
            return set().union(*all_achievements)

        @staticmethod
        def get_unique(player, all_players):
            """Get unique achievements of ONE player"""

            # Get all other players' achievements combined
            other = [p for p in all_players if p != player]
            other_achiev = (AchievementTracker.Analytics.get_all_unique(other))

            # Player archievements
            player_achiev = player.get_achievements()

            # Return what this player has that others don't
            unique_achiev = (player_achiev.difference(other_achiev))
            if not unique_achiev:
                return None
            return unique_achiev

        @staticmethod
        def get_diff(a, b):
            diff = a.difference(b)
            if not diff:
                return None
            return diff

        @staticmethod
        def get_common(players: list):
            """Get all common achievements across all players"""
            if not players:
                raise ValueError("Player list is empty")
            all_achievements = [
                player.get_achievements() for player in players
            ]
            common = set.intersection(*all_achievements)
            if not common:
                return None
            return common

        @staticmethod
        def get_achievements_summary(players):
            """Print a summary of unique and common achievements"""
            print("\n=== Achievement Analytics ===\n")
            unique = AchievementTracker.Analytics.get_all_unique(players)
            print(f"All unique achievements: {unique}")
            print(f"Total unique achievements count: {len(unique)}")
            common = AchievementTracker.Analytics.get_common(players)
            print(f"\nCommon to all players: {common}")
            print(
                f"Ultra rare achievements (1 player): "
                f"{AchievementTracker.Analytics.get_rare(players)}"
            )

        @staticmethod
        def get_rare(players):
            """Get rare achievements across all players"""
            all_achievements = {}
            for player in players:
                for achievement in player.get_achievements():
                    if achievement in all_achievements:
                        all_achievements[achievement] += 1
                    else:
                        all_achievements[achievement] = 1
            rare_achievements = {
                ach for ach, count in all_achievements.items() if count == 1
            }
            return rare_achievements


def ft_achievement_tracker():

    print("=== Achievement Tracker System ===\n")

    # initialize players and achievements
    AchievementTracker.create_achievements_examples()
    players = AchievementTracker.get_players()
    alice = players[0]
    bob = players[1]
    charlie = players[2]
    for achievements in players:
        print(achievements)

    print("\n=== Tests ===")
    # Testing set() is fonctionning properly by adding one already
    # existing achievement and checking achievements doesn't change
    print(
        f"\n- Try adding an already existant achievement: "
        f"'first_kill' to {alice.name}'s achievements"
    )
    before = alice.achievements
    alice.unlock('first_kill')
    after = alice.achievements
    print(f"Diff: {AchievementTracker.Analytics.get_diff(before, after)}")
    print(f"{alice.__str__()}")

    print("\n- Testing common achievements between players")
    print(
        "Alice vs Bob common: "
        f"{AchievementTracker.Analytics.get_common([alice, bob])}"
    )
    print(
        "Alice vs Charlie common: "
        f"{AchievementTracker.Analytics.get_common([alice, charlie])}"
    )
    # Testing to add a new player and
    # see if he's automatically added to players
    print("\n- Adding a new player: David")
    david = AchievementTracker("David")
    david.unlock_multiple(
        'first_kill', 'joyous_folk',
        'speed_demon', 'you_shall_not_pass', 'level_10')
    print(david)

    # Get unique achievements for each player
    print("\n- Unique achievements per player:")
    for player in players:
        player_unique = (
            AchievementTracker.Analytics.get_unique(player, players))
        print(f"Achievements ONLY {player.name} has: {player_unique}")

    # Finally call a summary of unique and commons achievements
    # as well as showing some stats about it
    AchievementTracker.Analytics.get_achievements_summary(players)

    print("\nThanks for using the Achievement Tracker System!\n")


if __name__ == "__main__":
    ft_achievement_tracker()
