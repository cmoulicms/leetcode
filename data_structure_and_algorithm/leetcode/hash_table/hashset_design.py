key = 1
class MyHashSet:

    def __init__(self):
        self.set = set()

    def add(self, key: int):
        self.set.add(key)

    def remove(self, key: int):
        self.set.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.set:
            return True
        else:
            return False

obj = MyHashSet()
obj.add(key)
obj.remove(key)
obj.contains(key)