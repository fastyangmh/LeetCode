# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # method1
        res = []

        def helper(node):
            if not node:
                return

            helper(node.left)
            res.append(node.val)
            helper(node.right)

        helper(root)

        return res

        # # method2
        # res = []
        # stack = []
        # curr = root

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left

        #     curr = stack.pop()
        #     res.append(curr.val)
        #     curr = curr.right

        # return res

        # # method3
        # res = []
        # curr = root

        # while curr:
        #     if not curr.left:
        #         res.append(curr.val)
        #         curr = curr.right
        #     else:
        #         pre = curr.left
        #         while pre.right and pre.right != curr:
        #             pre = pre.right

        #         if not pre.right:
        #             pre.right = curr
        #             curr = curr.left
        #         else:
        #             pre.right = None
        #             res.append(curr.val)
        #             curr = curr.right
        # return res
