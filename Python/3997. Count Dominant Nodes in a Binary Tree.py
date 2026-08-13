# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            left_val = dfs(node.left)
            right_val = dfs(node.right)
            maximum = max(node.val, left_val, right_val)

            if node.val == maximum:
                self.ans += 1

            return maximum

        dfs(root)

        return self.ans
