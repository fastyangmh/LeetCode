"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        # # method1
        # if not root:
        #     return None

        # queue = [root]

        # while queue:

        #     queue_size = len(queue)

        #     for idx in range(queue_size):
        #         node = queue.pop(0)

        #         if idx + 1 < queue_size:
        #             node.next = queue[0]

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        # return root

        # method2
        if not root:
            return None

        leftmost = root

        while leftmost.left:
            head = leftmost

            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root
