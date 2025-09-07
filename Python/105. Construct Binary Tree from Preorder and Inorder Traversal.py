# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder root -> left -> right
        # inorder left -> root -> right

        # method1
        # if not preorder or not inorder:
        #     return None

        # root_val = preorder[0]
        # root = TreeNode(root_val)

        # idx = inorder.index(root_val)

        # left_inorder = inorder[:idx]
        # right_inorder = inorder[idx + 1 :]

        # left_preorder = preorder[
        #     1 : 1 + len(left_inorder)
        # ]  # left-close right-open, so need to plus 1
        # right_preorder = preorder[1 + len(left_inorder) :]

        # root.left = self.buildTree(left_preorder, left_inorder)
        # root.right = self.buildTree(right_preorder, right_inorder)

        # return root

        # method2
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            idx = inorder_index[root_val]

            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)

            return root

        return helper(0, len(preorder) - 1)
