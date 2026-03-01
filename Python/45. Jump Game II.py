class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = end = steps = 0
        n = len(nums)

        for idx in range(n - 1):
            max_reach = max(max_reach, idx + nums[idx])

            if idx == end:
                steps += 1
                end = max_reach

                if end >= n - 1:
                    break

        return steps
