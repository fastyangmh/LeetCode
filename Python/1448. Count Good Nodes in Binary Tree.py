# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # # method1
        # def dfs(node, max_so_far):
        #     if not node:
        #         return 0

        #     count = 1 if node.val >= max_so_far else 0
        #     max_so_far = max(max_so_far, node.val)

        #     return count + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

        # return dfs(root, root.val)

        # method2
        ans = 0
        queue = deque([(root, root.val)])

        while queue:
            node, max_so_far = queue.popleft()

            if node.val >= max_so_far:
                ans += 1

            new_max = max(max_so_far, node.val)

            if node.left:
                queue.append((node.left, new_max))

            if node.right:
                queue.append((node.right, new_max))

        return ans
