class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        # time: O(n**2), space: O(1)
        n = len(nums)
        ans = 0

        for left in range(n):
            even_count = 0
            odd_count = 0

            for right in range(left, n):
                if nums[right] % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

                if odd_count > 0 and b * even_count <= a * odd_count:
                    ans += 1

        return ans
