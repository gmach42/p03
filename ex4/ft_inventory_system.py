#!/usr/bin/env python3

class Item:
    quantity: int = 0

    def __init__(self, name: str, price: int, type: str):
        self.name = name
        self.price = price
        self.type = type

    @classmethod
    def get_item_types(cls):
        return ['Weapon', 'Armor', 'Potion', 'Misc']

    @classmethod
    def get_quantity(cls):
        return cls.quantity

    def __str__(self):
        return f"{self.name} ({self.type}) - ${self.price} x {self.quantity}"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item, quantity: int = 1):
        for inv_item in self.items:
            if inv_item.name == item.name:
                inv_item.quantity += quantity
                return
        item.quantity = quantity
        self.items.append(item)

    def remove_item(self, item_name: str, quantity: int = 1):
        for inv_item in self.items:
            if inv_item.name == item_name:
                if inv_item.quantity >= quantity:
                    inv_item.quantity -= quantity
                    if inv_item.quantity == 0:
                        self.items.remove(inv_item)
                return

    def list_items(self):
        for item in self.items:
            print(item)

def main():
    print("=== Player Inventory System ===")


if __name__ == "__main__":
    main()
