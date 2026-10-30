class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        n = len(nums)
        equal = 0
        freq = {}
        max_gain = 0

        for i in range(n - 1):
            j = i + 1
            a, b = nums[i], nums[j]

            if a == b:
                equal += 1
            else:
                key = (min(a, b), max(a, b))
                freq[key] = freq.get(key, 0) + 1
                max_gain = max(max_gain, freq[key])

        return equal + max_gain
