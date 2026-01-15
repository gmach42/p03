# yield, next(), iter(), range(), len(), print(), for loops

def process_events(lst: list):
    events = iter(lst)
    for event in events:
        yield next(events)


def main():
    print("=== Game Data Stream Processor ===")

    print("\nProcessing 1000 game events...")
    with open("game_events.txt", 'r') as file:
        content = file.read()
    print(process_events(content))


if __name__ == "__main__":
    main()
