# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        parent = {}
        self.start_node = None

        def dfs(node, par):
            if not node:
                return

            parent[node] = par

            if node.val == start:
                self.start_node = node

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        visited = {self.start_node}
        queue = deque([(self.start_node, 0)])
        ans = 0

        while queue:
            node, t = queue.popleft()
            ans = max(ans, t)

            for nxt in (node.left, node.right, parent[node]):
                if nxt and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, t + 1))

        return ans
