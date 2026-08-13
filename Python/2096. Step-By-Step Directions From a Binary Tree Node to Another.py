# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        # method1
        def find_path(node, target, path):
            if not node:
                return False

            if node.val == target:
                return True

            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()

        start = []
        dest = []
        find_path(root, startValue, start)
        find_path(root, destValue, dest)

        i = 0

        while i < len(start) and i < len(dest) and start[i] == dest[i]:
            i += 1

        return "U" * (len(start) - i) + "".join(dest[i:])

        # # method2
        # parent = {}
        # start_node = None
        # dest_node = None

        # def dfs(node, par):
        #     nonlocal start_node, dest_node

        #     if not node:
        #         return

        #     parent[node] = par

        #     if node.val == startValue:
        #         start_node = node
        #     if node.val == destValue:
        #         dest_node = node

        #     dfs(node.left, node)
        #     dfs(node.right, node)

        # dfs(root, None)

        # queue = deque([(start_node, "")])
        # visited = {start_node}

        # while queue:
        #     node, path = queue.popleft()

        #     if node == dest_node:
        #         return path

        #     for directions, nxt_node in zip(
        #         ("L", "R", "U"), (node.left, node.right, parent[node])
        #     ):
        #         if not nxt_node or nxt_node in visited:
        #             continue

        #         visited.add(nxt_node)
        #         new_path = path + directions
        #         queue.append((nxt_node, new_path))
