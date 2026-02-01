# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # # method1
        # self.idx = 1

        # def inorder(node):
        #     if not node:
        #         return

        #     left = inorder(node.left)
        #     if left is not None:
        #         return left

        #     if self.idx == k:
        #         return node.val
        #     self.idx += 1

        #     right = inorder(node.right)
        #     if right is not None:
        #         return right

        # return inorder(root)

        # method2
        curr = root
        stack = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
