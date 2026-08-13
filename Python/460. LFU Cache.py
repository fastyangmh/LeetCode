class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.freq = 1

        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add_last(self, node):
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def remove_first(self):
        if self.size == 0:
            return

        node = self.head.next

        self.remove(node)

        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.nodes = {}

        self.freq_map = {}

        self.min_freq = 0

    def _increase_freq(self, node):
        old_freq = node.freq

        old_list = self.freq_map[old_freq]

        old_list.remove(node)

        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq += 1

        node.freq += 1

        new_freq = node.freq

        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()

        self.freq_map[new_freq].add_last(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]

        self._increase_freq(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._increase_freq(node)
            return

        if len(self.nodes) >= self.capacity:
            min_freq_list = self.freq_map[self.min_freq]

            node = min_freq_list.remove_first()

            del self.nodes[node.key]

        node = Node(key, value)
        self.nodes[key] = node

        if 1 not in self.freq_map:
            self.freq_map[1] = DoublyLinkedList()

        self.freq_map[1].add_last(node)
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
