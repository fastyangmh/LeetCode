class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        maximum = max(nums)
        flag = [False] * (maximum + 1)

        for i in nums:
            flag[i] = True

        div = [0] * (maximum + 1)

        for i in range(1, maximum + 1):
            if not flag[i]:
                continue

            for j in range(i, maximum + 1, i):
                if div[j] == 0:
                    div[j] = i

        return sum(div[i] for i in nums)
