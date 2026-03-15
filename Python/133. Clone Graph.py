"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # # method1
        # if not node:
        #     return node

        # old_to_new = {}

        # def dfs(curr):
        #     if curr in old_to_new:
        #         return old_to_new[curr]

        #     clone = Node(curr.val)
        #     old_to_new[curr] = clone

        #     for neighbor in curr.neighbors:
        #         clone.neighbors.append(dfs(neighbor))

        #     return clone

        # dfs(node)

        # return old_to_new[node]

        # method2
        if not node:
            return

        old_to_new = {}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            if curr not in old_to_new:
                old_to_new[curr] = Node(curr.val)

            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    queue.append(neighbor)
                    old_to_new[neighbor] = Node(neighbor.val)

                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]
