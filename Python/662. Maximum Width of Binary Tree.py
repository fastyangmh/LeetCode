# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        ans = 0

        while queue:
            _, left = queue[0]
            _, right = queue[-1]
            ans = max(ans, right - left + 1)

            for _ in range(len(queue)):
                node, idx = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * idx + 1))
                if node.right:
                    queue.append((node.right, 2 * idx + 2))

        return ans
