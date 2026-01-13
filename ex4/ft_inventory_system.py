#!/usr/bin/env python3

class Item:
    def __init__(
            self, name: str, price: int, type: str,
            quantity: int, rarity: str
            ):
        self.name = name.capitalize()
        self.price = price
        self.type = type.capitalize()
        self.quantity = quantity
        self.rarity = rarity

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.type}, {self.rarity}): "
            f"{self.quantity}x @ {self.price} gold each = "
            f"{self.price * self.quantity} gold"
        )


class Inventory:
    def __init__(self, owner: str):
        self.owner = owner
        self.items = {}

    def add_items(self, items):
        for item in items:
            if item.name in self.items:
                self.items[item.name].quantity += item.quantity
            else:
                self.items[item.name] = item

    def remove_item(self, item_name: str):
        if item_name in self.items:
            del self.items[item_name]

    def get_item(self, item_name: str):
        return self.items.get(item_name)

    def items_count(self) -> int:
        count = 0
        for item in self.items.values():
            count += item.quantity
        return count

    def inventory_value(self) -> int:
        value = 0
        for item in self.items.values():
            value += (item.price * item.quantity)
        return value

    def count_by_type(self) -> dict:
        type_count = {}
        for item in self.items.values():
            if item.type in type_count:
                type_count[item.type] += item.quantity
            else:
                type_count[item.type] = item.quantity
        return type_count

    @staticmethod
    def format_dict(d: dict) -> str:
        formatted = ", ".join(f"{key} ({value})" for key, value in d.items())
        return formatted

    def item_summary(self, item_name: str):
        item = self.get_item(item_name.capitalize())
        if item:
            print(item)
        else:
            print(f"\nItem '{item_name}' not found in inventory.\n")

    def inventory_summary(self):
        print(f"\n=== {self.owner}'s Inventory ===\n")
        for item in self.items.values():
            print(item)
        print(
            f"\nTotal Items: {self.items_count()}\n"
            f"Total Value: {self.inventory_value()} gold"
        )
        print(
            f"Items by Type: {self.format_dict(self.count_by_type())}")


def main():
    print("=== Player Inventory System ===")
    alice = Inventory("Alice")
    alice.add_items([
        Item("sword", 500, "Weapon", 1, "rare"),
        Item("potion", 50, "Consumable", 5, "common"),
        Item("shield", 200, "Armor", 1, "uncommon")
    ])
    alice.inventory_summary()
    print("\n-- Adding more potions to Alice's inventory --")
    alice.add_items([Item("potion", 50, "Consumable", 3, "common")])
    alice.item_summary("potion")


if __name__ == "__main__":
    main()
