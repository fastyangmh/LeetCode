class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        write = n - 1
        left, right = 0, n - 1

        while left <= right:
            l, r = nums[left], nums[right]

            if abs(l) >= abs(r):
                result[write] = l * l
                left += 1
            else:
                result[write] = r * r
                right -= 1
            write -= 1

        return result
