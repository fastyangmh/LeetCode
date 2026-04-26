class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # # method1
        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     a = nums[i]

        #     for j in range(i + 1, n):
        #         b = nums[j]

        #         count += 1 if a == b else 0

        # return count

        # method2
        ans = 0
        count = {}

        for num in nums:
            ans += count.get(num, 0)
            count[num] = count.get(num, 0) + 1

        return ans
