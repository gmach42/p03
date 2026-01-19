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
        def stream_analytics(cls) -> None:
            print("\n=== Stream Analytics ===\n")
            print(
                f"Total events processed: {cls.events_processed}\n"
                f"{len(cls.high_levels)} High-level players (+10):\n"
                f"{cls.high_levels}\n"
                f"Treasure events: {cls.treasure_events}\n"
                f"Level-up events: {cls.levelup_events}\n"
            )


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


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

        merlin.Analytics.stream_analytics()
    except FileNotFoundError:
        print("Please add a game_events.txt file")
    except TypeError:
        print(
            "Please verify that the events are correctly "
            "implemented in your game_events.txt file"
        )

    print("\n=== Generator Demonstration ===\n")
    # 10 Fibonacci numbers
    fib_gen = fibonacci(100)
    fib_to_print = ""
    for num in range(10):
        if num == 0:
            fib_to_print += f"{next(fib_gen)}"
        else:
            fib_to_print += f", {next(fib_gen)}"
    print(f"Fibonacci sequence (first 10 numbers): {fib_to_print}")

    # First 5 prime numbers
    prime_gen = (num for num in range(2, 100) if is_prime(num))
    prime_to_print = ""
    for num in range(5):
        if num == 0:
            prime_to_print += f"{next(prime_gen)}"
        else:
            prime_to_print += f", {next(prime_gen)}"
    print(f"Prime numbers (first 5 primes): {prime_to_print}")


if __name__ == "__main__":
    main()
