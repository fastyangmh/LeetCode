# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # method1
        if not nums:
            return

        mid_idx = len(nums) // 2
        node = TreeNode(nums[mid_idx])
        node.left = self.sortedArrayToBST(nums[:mid_idx])
        node.right = self.sortedArrayToBST(nums[mid_idx + 1 :])

        return node

        # # method2
        # def helper(left, right):
        #     if left > right:
        #         return None

        #     mid = (left + right) // 2

        #     node = TreeNode(nums[mid])

        #     node.left = helper(left, mid - 1)
        #     node.right = helper(mid + 1, right)

        #     return node

        # return helper(0, len(nums) - 1)
