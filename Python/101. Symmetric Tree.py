# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # method1
        def is_mirror(n1, n2):
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            return (
                n1.val == n2.val
                and is_mirror(n1.left, n2.right)
                and is_mirror(n1.right, n2.left)
            )

        return is_mirror(root.left, root.right)

        # # method2
        # q = [(root.left, root.right)]

        # while q:
        #     n1, n2 = q.pop(0)

        #     if not n1 and not n2:
        #         continue

        #     if not n1 or not n2:
        #         return False

        #     if n1.val != n2.val:
        #         return False

        #     q.append((n1.left, n2.right))
        #     q.append((n1.right, n2.left))

        # return True
