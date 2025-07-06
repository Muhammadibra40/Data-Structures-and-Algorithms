class UniqueList:
    def __init__(self):
        self._data = {}      # Internal dictionary {id: item}
        self._order = []     # Keeps the order of IDs
        self._next_id = 0    # Auto-increment ID
    
    def add(self, item):
        """Add item with a unique ID."""
        item_id = self._next_id
        self._data[item_id] = item
        self._order.append(item_id)
        self._next_id += 1
        return item_id  # Return the ID assigned
    
    def get_by_index(self, index):
        """Access item by position (like a list)."""
        item_id = self._order[index]
        return self._data[item_id]
    
    def get_by_id(self, item_id):
        """Access item by its unique ID."""
        return self._data.get(item_id, None)
    
    def remove_by_id(self, item_id):
        """Remove item by ID."""
        if item_id in self._data:
            self._order.remove(item_id)
            del self._data[item_id]
    
    def __len__(self):
        return len(self._order)
    
    def __str__(self):
        return str([self._data[item_id] for item_id in self._order])



ulist = UniqueList()
id1 = ulist.add("Apple")
id2 = ulist.add("Banana")
id3 = ulist.add("Cherry")

print(ulist)  # ['Apple', 'Banana', 'Cherry']

print(ulist.get_by_index(1))  # Banana
print(ulist.get_by_id(id3))   # Cherry

ulist.remove_by_id(id2)
print(ulist)  # ['Apple', 'Cherry']
