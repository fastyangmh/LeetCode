class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float("inf")

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                if abs(target - curr_sum) < abs(target - ans):
                    ans = curr_sum

                if curr_sum < target:
                    j += 1
                elif curr_sum > target:
                    k -= 1
                else:
                    return curr_sum

        return ans
