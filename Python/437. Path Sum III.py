# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        prefix = {0: 1}

        def dfs(node, curr):
            if not node:
                return

            curr += node.val
            self.ans += prefix.get(curr - targetSum, 0)

            prefix[curr] = prefix.get(curr, 0) + 1

            dfs(node.left, curr)
            dfs(node.right, curr)

            prefix[curr] -= 1

        dfs(root, 0)

        return self.ans
