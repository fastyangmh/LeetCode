# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # method1
        # def dfs(node, low, high):
        #     if not node:
        #         return True

        #     if not (low < node.val < high):
        #         return False

        #     return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        # return dfs(root, float("-inf"), float("inf"))

        # method2
        prev = None

        def inorder(node):
            nonlocal prev
            
            if not node:
                return True

            if not inorder(node.left):
                return False

            if prev is not None and node.val <= prev:
                return False

            prev = node.val

            return inorder(node.right)

        return inorder(root)
