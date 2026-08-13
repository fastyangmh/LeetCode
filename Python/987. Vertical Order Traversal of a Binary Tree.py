# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # method1
        # ret = {}

        # def dfs(node, row, col):
        #     if not node:
        #         return

        #     if col not in ret:
        #         ret[col] = []

        #     heapq.heappush(ret[col], (row, node.val))

        #     dfs(node.left, row + 1, col - 1)
        #     dfs(node.right, row + 1, col + 1)

        # dfs(root, 0, 0)

        # cols = sorted(ret.keys())
        # ans = []

        # for col in cols:
        #     tmp = []
        #     while ret[col]:
        #         tmp.append(heapq.heappop(ret[col])[1])
        #     ans.append(tmp)

        # return ans

        # method2
        nodes = []

        def dfs(node, row, col):
            if not node:
                return

            nodes.append((col, row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        nodes.sort()

        ans = []
        prev_col = None

        for col, row, val in nodes:
            if col != prev_col:
                ans.append([])
                prev_col = col

            ans[-1].append(val)

        return ans
