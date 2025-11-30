class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.tail = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        node = self.tail.prev

        self._remove_node(node)

        return node

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1

        self._move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self._add_node(new_node)
            self.cache[key] = new_node

            if len(self.cache) > self.capacity:
                node = self._pop_tail()

                del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
