# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # # method1
        # def dfs(pre, ino):
        #     if not pre or not ino:
        #         return None

        #     root = TreeNode(pre[0])

        #     in_idx = ino.index(root.val)

        #     left_ino = ino[:in_idx]
        #     right_ino = ino[in_idx + 1 :]

        #     left_pre = pre[1 : 1 + len(left_ino)]
        #     right_pre = pre[1 + len(left_ino) :]

        #     root.left = dfs(left_pre, left_ino)
        #     root.right = dfs(right_pre, right_ino)

        #     return root

        # return dfs(preorder, inorder)

        # method2
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1

            in_idx = inorder_map[root.val]

            root.left = helper(left, in_idx - 1)
            root.right = helper(in_idx + 1, right)

            return root

        return helper(0, len(preorder) - 1)
