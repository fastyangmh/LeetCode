import bisect


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        left_nums = nums[:n]
        right_nums = nums[n:]

        left = [[] for _ in range(n + 1)]
        right = [[] for _ in range(n + 1)]

        for mask in range(2**n):
            left_sum = right_sum = 0
            count = 0

            for i in range(n):
                if mask & (1 << i):
                    left_sum += left_nums[i]
                    right_sum += right_nums[i]
                    count += 1

            left[count].append(left_sum)
            right[count].append(right_sum)

        for k in range(n + 1):
            right[k].sort()

        total = sum(nums)
        ans = float("inf")

        for k in range(n + 1):
            right_sums = right[n - k]

            for left_sum in left[k]:
                target = total / 2 - left_sum

                idx = bisect.bisect_left(right_sums, target)

                if idx < len(right_sums):
                    chosen_sum = left_sum + right_sums[idx]
                    ans = min(ans, abs(2 * chosen_sum - total))

                if idx > 0:
                    chosen_sum = left_sum + right_sums[idx - 1]
                    ans = min(ans, abs(2 * chosen_sum - total))
        return ans
