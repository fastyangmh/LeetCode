class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        ans = 0
        max_range = 0

        for num in nums:
            s = str(num)
            curr_range = ord(max(s)) - ord(min(s))

            if curr_range > max_range:
                ans = num
                max_range = curr_range
            elif curr_range == max_range:
                ans += num

        return ans
