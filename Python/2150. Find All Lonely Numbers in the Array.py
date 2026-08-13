from collections import Counter


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []

        for num in nums:
            if counter[num] == 1 and num - 1 not in counter and num + 1 not in counter:
                ans.append(num)

        return ans
