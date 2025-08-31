# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # method1
        if not root:
            return []

        q = [root]
        rets = []

        while q:
            tmp = []

            for _ in range(len(q)):
                node = q.pop(0)
                tmp.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            rets.append(tmp)

        return rets

        # # method2
        # res = []

        # def dfs(node, depth):
        #     if not node:
        #         return

        #     if len(res) == depth:
        #         res.append([])

        #     res[depth].append(node.val)

        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)

        # dfs(root, 0)

        # return res
