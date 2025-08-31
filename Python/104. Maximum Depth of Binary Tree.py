# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs method
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # # bfs method
        # if not root:
        #     return 0

        # q = [root]
        # depth = 0

        # while q:
        #     depth += 1

        #     for _ in range(len(q)):
        #         node = q.pop(0)

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return depth
