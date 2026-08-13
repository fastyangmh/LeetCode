import random


class Solution:
    def __init__(self, w: List[int]):
        prefix = [w[0]]

        for i in range(1, len(w)):
            prefix.append(prefix[-1] + w[i])

        self.prefix = prefix

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[-1])

        left, right = 0, len(self.prefix) - 1

        while left < right:
            mid = (left + right) // 2

            if self.prefix[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
