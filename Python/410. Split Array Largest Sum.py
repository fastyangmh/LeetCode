class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def check(limit):
            groups = 1
            curr = 0

            for num in nums:
                if curr + num > limit:
                    groups += 1
                    curr = num
                else:
                    curr += num

            return groups <= k

        l, r = max(nums), sum(nums)

        while l < r:
            m = (l + r) // 2

            if check(m):
                r = m
            else:
                l = m + 1

        return l
