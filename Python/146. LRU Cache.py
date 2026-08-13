class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _remove_first(self):
        node = self.head.next

        self._remove(node)

        return node

    def _add_last(self, node):
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]

        self._remove(node)
        self._add_last(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value

            self._remove(node)
            self._add_last(node)
            return

        if len(self.nodes) >= self.capacity:
            node = self._remove_first()

            self._remove(node)

            del self.nodes[node.key]

        node = Node(key, value)
        self.nodes[key] = node

        self._add_last(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
