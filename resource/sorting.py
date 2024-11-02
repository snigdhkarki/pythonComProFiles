from functools import cmp_to_key

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price}"

def compare_price(item1, item2):
    if item1.price < item2.price:
        return -1
    elif item1.price > item2.price:
        return 1
    else:
        return 0

items = [
    Item("Laptop", 1200),
    Item("Phone", 300),
    Item("Tablet", 800),
    Item("Monitor", 250)
]

sorted_items = sorted(items, key=cmp_to_key(compare_price))

# print("Items sorted by price:")
# for item in sorted_items:
#     print(item)