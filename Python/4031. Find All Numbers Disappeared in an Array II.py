class Solution:
    def findDisappearedNumbers(
        self, nums: list[int], lower: int, upper: int
    ) -> list[list[int]]:
        # method1
        # unique = set(nums)
        # i = lower
        # ans = []

        # while i < upper + 1:
        #     if i in unique:
        #         i += 1
        #         continue

        #     j = i

        #     while j < upper + 1 and j not in unique:
        #         j += 1

        #     start, end = i, j - 1

        #     ans.append([start, end])

        #     i = j

        # return ans

        # # method2
        unique = set(nums)
        ans = []
        start = None

        for x in range(lower, upper + 1):
            if x not in unique:
                if start is None:
                    start = x
            elif start is not None:
                ans.append([start, x - 1])
                start = None

        if start is not None:
            ans.append([start, upper])

        return ans
