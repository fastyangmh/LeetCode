# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # method1
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

        # # method2
        # self.count = 0
        # self.res = None

        # def inorder(node):
        #     if not node or self.res is not None:
        #         return None

        #     inorder(node.left)
        #     self.count += 1
        #     if self.count == k:
        #         self.res = node.val
        #         return
        #     inorder(node.right)

        # inorder(root)

        # return self.res
