# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def dfs(node, par):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        queue = deque([target])
        visited = {target}
        dist = 0

        while queue:
            if dist == k:
                return [node.val for node in queue]

            for _ in range(len(queue)):
                node = queue.popleft()

                for nxt in (node.left, node.right, parent[node]):
                    if not nxt or nxt in visited:
                        continue
                    visited.add(nxt)
                    queue.append(nxt)

            dist += 1

        return []
