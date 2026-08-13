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

        curr = head
        dummy = new = Node(0)

        while curr:
            new.next = curr.next
            curr.next = curr.next.next

            new = new.next
            curr = curr.next

        return dummy.next
