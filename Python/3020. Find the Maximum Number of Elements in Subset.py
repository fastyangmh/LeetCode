from collections import Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 1

        for num in counter:
            if num == 1:
                if counter[num] % 2 == 0:
                    ans = max(ans, counter[num] - 1)
                else:
                    ans = max(ans, counter[num])
                continue

            curr = num
            length = 0

            while True:
                if counter[curr] >= 2:
                    length += 2
                    curr *= curr
                else:
                    break

            if counter[curr] == 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans
