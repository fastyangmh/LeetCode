# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # # method1
        # if not root:
        #     return []

        # queue = deque([root])
        # res = []

        # while queue:

        #     l = len(queue)

        #     for idx in range(l):
        #         node = queue.popleft()

        #         if idx == l - 1:
        #             res.append(node.val)

        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)

        # return res

        # method2
        res = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return res
