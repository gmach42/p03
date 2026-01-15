# yield, next(), iter(), range(), len(), print(), for loops

class StreamWizard:
    def __init__(self, name):
        self.name = name
        self.events = []

    def events_generator(events: list[dict]):
        for event in events:
            try:
                yield (
                    f"Event {event['id']}: "
                    f"Player {event['player']} "
                    f"({event['level']}) {event['event_type']}"
                )
            except KeyError as e:
                print(f"KeyError: {e}")

    class Analytics:

        @staticmethod
        def total_events(events: list) -> int:
            return len(events)

        @staticmethod
        def total_hl(events: list) -> int:
            hl = 0
            for event in events:
                if event['level'] >= 10:
                    hl += 1
            return hl

        @staticmethod
        def total_treasures(events: list) -> int:
            treasures = 0
            for event in events:
                if event['event_type'] == "item_found":
                    treasures += 1
            return treasures

        def total_lvlup(events: list) -> int:
            lvlup = 0
            for event in events:
                if event['event_type'] == "level_up":
                    lvlup += 1
            return lvlup

        @staticmethod
        def stream_analytics(events: list) -> None:
            print("=== Stream Analytics ===\n")
            print(f"Total events processed: {StreamWizard.Analytics.total_events(events)}")
            print(f"High-level players (+10): {StreamWizard.Analytics.total_hl}")
            print(f"Treasure events: {StreamWizard.Analytics.total_treasures(events)}")
            print(f"Level-up events: {StreamWizard.Analytics.total_lvlup(events)}")

def main():
    print("=== Game Data Stream Processor ===")

    merlin = StreamWizard("Merlin")

    print("\nProcessing 1000 game events...")
    test = [
        {"id": 1, "player": "alice", "level": 3, "event_type": "kill monster"},
        {"id": 2, "player": "bob", "level": 5,"event_type": "save monster"},
    ]
    event_stream = process_events(test)

    for _ in range(2):
        print(next(event_stream))
    # with open("game_events.txt", 'r') as file:
    #     content = file.read()
    # events = iter(process_events(content))
    # for event in range(3):
    #     print(next(events))
    # print(next(events))


if __name__ == "__main__":
    main()
