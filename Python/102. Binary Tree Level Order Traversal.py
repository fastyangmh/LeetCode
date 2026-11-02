# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            ans.append([])

            for _ in range(len(queue)):
                node = queue.popleft()

                ans[-1].append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return ans
