class RandomizedSet:
    def __init__(self):
        self._dict = {}
        self._list = []

    def insert(self, val: int) -> bool:
        if val in self._dict:
            return False

        self._dict[val] = len(self._list)
        self._list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self._dict:
            return False

        idx = self._dict[val]
        last = self._list[-1]

        self._list[idx] = last
        self._dict[last] = idx

        self._list.pop()
        self._dict.pop(val)

        return True

    def getRandom(self) -> int:
        import random

        return random.choice(self._list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
