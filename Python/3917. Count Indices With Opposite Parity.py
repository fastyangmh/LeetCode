class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        even_count = odd_count = 0

        for i in range(n - 1, -1, -1):
            is_odd = nums[i] % 2 == 1

            if is_odd:
                ans[i] += even_count
                odd_count += 1
            else:
                ans[i] += odd_count
                even_count += 1

        return ans
