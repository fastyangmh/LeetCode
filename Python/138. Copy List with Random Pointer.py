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
        curr = head

        while curr:
            new = Node(curr.val, next=curr.next)

            curr.next = new
            curr = new.next

        curr = head

        while curr:
            if curr.random:
                curr.next.random = curr.random.next

            curr = curr.next.next

        dummy = cloned = Node(0)
        curr = head

        while curr:
            cloned.next = curr.next

            cloned = cloned.next
            curr = curr.next.next

        return dummy.next
