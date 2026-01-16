# yield, next(), iter(), range(), len(), print(), for loops


class StreamWizard:
    def __init__(self, name):
        self.name = name
        self.events = []

    def events_generator(self, events: list[dict]):
        for event in events:
            try:
                StreamWizard.Analytics.counters(event)
                # Skip login / logout events
                if (
                    event["event_type"] == "login"
                    or event["event_type"] == "logout"
                ):
                    continue

                yield (
                    f"Event {event['id']}: "
                    f"Player {event['player']} "
                    f"(Level {event['data']['level']}) {event['event_type']}"
                )
            except KeyError as e:
                print(f"KeyError: {e}")

    class Analytics:
        events_processed = 0
        high_levels = []
        treasure_events = 0
        levelup_events = 0

        @classmethod
        def total_events(cls) -> int:
            return cls.total_events

        @staticmethod
        def total_hl(events: list) -> int:
            hl = 0
            for event in events:
                if event["data"]["level"] >= 10:
                    hl += 1
            return hl

        @staticmethod
        def total_treasures(events: list) -> int:
            treasures = 0
            for event in events:
                if event["event_type"] == "item_found":
                    treasures += 1
            return treasures

        @staticmethod
        def total_lvlup(events: list) -> int:
            lvlup = 0
            for event in events:
                if event["event_type"] == "level_up":
                    lvlup += 1
            return lvlup

        @classmethod
        def counters(cls, event: dict) -> None:
            cls.events_processed += 1
            if event["player"] not in cls.high_levels:
                if event["data"]["level"] >= 10:
                    cls.high_levels.append(event["player"])
            if event["event_type"] == "item_found":
                cls.treasure_events += 1
            if event["event_type"] == "level_up":
                cls.levelup_events += 1

        @classmethod
        def stream_analytics(cls, events: list) -> None:
            print("\n=== Stream Analytics ===\n")
            print(
                f"Total events processed: {cls.events_processed}\n"
                f"{len(cls.high_levels)} High-level players (+10):\n"
                f"{cls.high_levels}\n"
                f"Treasure events: {cls.treasure_events}\n"
                f"Level-up events: {cls.levelup_events}\n"
            )


def main():
    print("=== Game Data Stream Processor ===")

    merlin = StreamWizard("Merlin")

    print("\nProcessing 2 test events...")
    test = [
        {
            "id": "1",
            "player": "alice",
            "data": {"level": 3},
            "event_type": "kill monster",
        },
        {
            "id": 2,
            "player": "bob",
            "data": {"level": 5},
            "event_type": "save monster",
        },
    ]
    test_stream = merlin.events_generator(test)

    for _ in range(2):
        print(next(test_stream))

    print("\nProcessing lots of game events...\n")
    try:
        # Using eval() here to transform the string into a readable list
        with open("game_events.txt", "r") as file:
            content = eval(file.read())

        event_stream = merlin.events_generator(content)
        for event in event_stream:
            print(event)

        merlin.Analytics.stream_analytics(event_stream)
    except FileNotFoundError:
        print("Please add a game_events.txt file")
    except TypeError:
        print(
            "Please verify that the events are correctly "
            "implemented in your game_events.txt file"
        )


if __name__ == "__main__":
    main()
