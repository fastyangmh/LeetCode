# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # # method1
        # self.prev = None

        # def dfs(node):
        #     if not node:
        #         return node

        #     dfs(node.right)
        #     dfs(node.left)

        #     node.right = self.prev
        #     node.left = None
        #     self.prev = node

        # dfs(root)

        # method2
        curr = root

        while curr:
            if curr.left:
                predecessor = curr.left

                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
