class Inventory:

    def __init__(self, capacity):
        self._capacity = capacity
        self.items = []

    def add_item(self, item):
        if self._capacity > len(self.items):
            self.items.append(item)
        return 'not enough room in the inventory'

    def get_capacity(self):
        return self._capacity

    def __repr__(self):
        items_names = ', '.join(self.items)
        left_capacity = self._capacity - len(self.items)
        return f'Items: {items_names}.\nCapacity left: {left_capacity}'

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
