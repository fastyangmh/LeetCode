class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        cnt = [0] * 101

        for i in nums:
            cnt[i] += 1

        ans = []

        for _ in range(max(cnt)):
            for i in range(1, 101):
                if cnt[i] > 0:
                    ans.append(i)
                    cnt[i] -= 1

        return ans
