class Solution:
    def trap(self, height: List[int]) -> int:
        # # method 1
        # n = len(height)
        # left_max = [0] * n
        # right_max = [0] * n
        # res = 0

        # left_max[0] = height[0]
        # right_max[-1] = height[-1]

        # for idx in range(1, n):
        #     left_max[idx] = max(left_max[idx - 1], height[idx])

        # for idx in range(n - 2, -1, -1):
        #     right_max[idx] = max(right_max[idx + 1], height[idx])

        # for idx in range(n):
        #     res += max(0, min(left_max[idx], right_max[idx]) - height[idx])

        # return res

        # method2
        l, r = 0, len(height) - 1
        left_max = right_max = ans = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    ans += left_max - height[l]
                l += 1
            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    ans += right_max - height[r]
                r -= 1

        return ans
