class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
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

        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
