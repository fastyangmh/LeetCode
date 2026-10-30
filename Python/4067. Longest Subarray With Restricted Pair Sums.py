class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        MAX_NUM = 500

        last = [-1] * (MAX_NUM + 1)
        prev = [-1] * (MAX_NUM + 1)

        left = 0
        ans = 0

        for right, x in enumerate(nums):
            for a in range(1, x // 2 + 1):  # a<=b, b=x-a; a<=x-a; 2a<=x; a<=x/2
                b = x - a

                if a == b:
                    if prev[a] != -1:
                        left = max(left, prev[a] + 1)
                else:
                    if last[a] != -1 and last[b] != -1:
                        left = max(left, min(last[a], last[b]) + 1)

            for a in range(1, MAX_NUM - x + 1):
                b = x + a

                if last[a] != -1 and last[b] != -1:
                    left = max(left, min(last[a], last[b]) + 1)

            ans = max(ans, right - left + 1)

            prev[x] = last[x]
            last[x] = right

        return ans
