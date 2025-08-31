from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.orig = nums[:]

    def reset(self) -> List[int]:
        return self.orig[:]

    def shuffle(self) -> List[int]:
        arr = self.orig[:]
        n = len(arr)

        for i in range(n - 1, -1, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]

        return arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
