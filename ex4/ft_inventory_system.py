#!/usr/bin/env python3

import sys

from secretstorage import Item


# class Item:
#     def __init__(
#             self, name: str, price: int, type: str,
#             quantity: int, rarity: str
#             ):
#         self.name = name.capitalize()
#         self.price = price
#         self.type = type.capitalize()
#         self.quantity = quantity
#         self.rarity = rarity

#     def __str__(self) -> str:
#         return (
#             f"{self.name} ({self.type}, {self.rarity}): "
#             f"{self.quantity}x @ {self.price} gold each = "
#             f"{self.price * self.quantity} gold"
#         )


# class Inventory:
#     def __init__(self, owner: str):
#         self.owner = owner
#         self.items = {}

#     def add_items(self, items):
#         for item in items:
#             if item.name in self.items:
#                 self.items[item.name].quantity += item.quantity
#             else:
#                 self.items[item.name] = item

#     def remove_item(self, item_name: str):
#         if item_name in self.items:
#             del self.items[item_name]

#     def get_item(self, item_name: str):
#         return self.items.get(item_name)

#     def items_count(self) -> int:
#         count = 0
#         for item in self.items.values():
#             count += item.quantity
#         return count

#     def inventory_value(self) -> int:
#         value = 0
#         for item in self.items.values():
#             value += (item.price * item.quantity)
#         return value

#     def count_by_type(self) -> dict:
#         type_count = {}
#         for item in self.items.values():
#             if item.type in type_count:
#                 type_count[item.type] += item.quantity
#             else:
#                 type_count[item.type] = item.quantity
#         return type_count

#     @staticmethod
#     def format_dict(d: dict) -> str:
#         formatted = ", ".join(f"{key} ({value})" for key, value in d.items())
#         return formatted

#     def item_summary(self, item_name: str):
#         item = self.get_item(item_name.capitalize())
#         if item:
#             print(item)
#         else:
#             print(f"\nItem '{item_name}' not found in inventory.\n")

#     def inventory_summary(self):
#         print(f"\n=== {self.owner}'s Inventory ===\n")
#         for item in self.items.values():
#             print(item)
#         print(
#             f"\nTotal Items: {self.items_count()}\n"
#             f"Total Value: {self.inventory_value()} gold"
#         )
#         print(
#             f"Items by Type: {self.format_dict(self.count_by_type())}")


# def main():
#     print("=== Player Inventory System ===")
#     alice = Inventory("Alice")
#     alice.add_items([
#         Item("sword", 500, "Weapon", 1, "rare"),
#         Item("potion", 50, "Consumable", 5, "common"),
#         Item("shield", 200, "Armor", 1, "uncommon")
#     ])
#     alice.inventory_summary()
#     print("\n-- Adding more potions to Alice's inventory --")
#     alice.add_items([Item("potion", 50, "Consumable", 3, "common")])
#     alice.item_summary("potion")


# if __name__ == "__main__":
#     main()


class InventoryMaster:
    def __init__(self):
        self.objs = {}

    def total_items(self) -> int:
        return sum(self.objs.values())

    def add_item(self, obj_name: str, quantity: int) -> None:
        self.objs.update({obj_name: quantity})

    def remove_item(self, obj_name: str) -> None:
        self.objs.pop(obj_name)

    @staticmethod
    def format_dict(d: dict) -> str:
        formatted = ", ".join(f"{key} ({value})" for key, value in d.items())
        return formatted

    @staticmethod
    def percentage_inventory(q_item: int, total: int) -> float:
        if total == 0:
            return 0.0
        return (q_item / total) * 100.0

    def display_inventory(self) -> None:
        for obj in self.objs.keys():
            print(
                f"{obj}: {self.objs[obj]} units "
                f"({self.percentage_inventory(self.objs[obj], self.total_items()):.1f}%)"
            )

    def most_abundant_item(self) -> str:
        if not self.objs:
            return None
        return max(self.objs, key=self.objs.get)

    def least_abundant_item(self) -> str:
        if not self.objs:
            return None
        return min(self.objs, key=self.objs.get)

    def items_by_category(self) -> dict:
        Abundant = {}
        Moderate = {}
        Scarce = {}
        for obj in self.objs.keys():
            qty = self.objs[obj]
            if qty >= 10:
                Abundant[obj] = qty
            elif 2 <= qty < 10:
                Moderate[obj] = qty
            else:
                Scarce[obj] = qty
        return {"Abundant": Abundant, "Moderate": Moderate, "Scarce": Scarce}

    def restock_suggestions(self) -> list:
        suggestions = []
        for obj in self.objs.keys():
            if self.objs[obj] < 2:
                suggestions.append(obj)
        return suggestions


def ft_inventory_system():
    print("=== Player Inventory System ===")
    if len(sys.argv) < 2:
        print(
            "No inventory data provided. Usage: python3 "
            "ft_inventory_system.py <item1:nb> <item2:nb> ..."
        )
        return
    inv = InventoryMaster()
    for i in range(1, len(sys.argv)):
        try:
            name, qty = sys.argv[i].split(":")
            inv.add_item(name, int(qty))
        except (IndexError, ValueError) as e:
            print(f"Error: Invalid item format '{sys.argv[i]}':\n{e}\n")
            return

    print(f"Total items in inventory: {inv.total_items()}")
    print(f"Unique item types: {len(inv.objs)}")

    print("\n=== Current Inventory ===")
    inv.display_inventory()

    print("\n=== Inventory Statistics ===")
    most_abundant = inv.most_abundant_item()
    print(
        f"Most abundant: "
        f"{most_abundant} "
        f"({inv.objs.get(most_abundant)} units)"
    )
    least_abundant = inv.least_abundant_item()
    print(
        f"Least abundant: "
        f"{least_abundant} "
        f"({inv.objs.get(least_abundant)} units)"
    )

    print("\n=== Item Categories ===")
    categories = inv.items_by_category()
    for category, items in categories.items():
        if category and items:
            print(f"{category} items: {InventoryMaster.format_dict(items)}")

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {inv.restock_suggestions()}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inv.objs.keys())}")
    print(f"Dictionary values: {list(inv.objs.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inv.objs}")


if __name__ == "__main__":
    ft_inventory_system()
