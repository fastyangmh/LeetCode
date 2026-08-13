class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        jumps = 0
        max_reach = 0

        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == end:
                jumps += 1
                end = max_reach

                if end >= n - 1:
                    return jumps

        return jumps
