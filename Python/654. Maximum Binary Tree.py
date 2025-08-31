# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:        
        if not nums:
            return

        max_num = max(nums)
        max_num_idx = nums.index(max_num)
        root = TreeNode(max_num)

        root.right = self.constructMaximumBinaryTree(nums[max_num_idx + 1 :])
        root.left = self.constructMaximumBinaryTree(nums[:max_num_idx])

        return root
