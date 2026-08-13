class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        min_num = float("inf")
        max_num = float("-inf")

        for num in nums:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

        return (max_num - min_num) * k
