"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # # method1
        # node_mapping = {}
        # dummy = curr = Node(0)
        # node = head

        # while node:
        #     curr.next = Node(node.val)
        #     node_mapping[node] = curr.next
        #     curr, node = curr.next, node.next

        # node = head
        # curr = dummy.next

        # while node:
        #     if node.random in node_mapping:
        #         curr.random = node_mapping[node.random]
        #     curr, node = curr.next, node.next

        # return dummy.next

        # method2
        curr = head

        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next

        curr = head

        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        dummy = new = Node(0)

        while curr:
            new.next = curr.next
            curr.next = curr.next.next

            curr = curr.next
            new = new.next

        return dummy.next
