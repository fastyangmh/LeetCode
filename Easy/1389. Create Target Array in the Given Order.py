class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for idx, n in enumerate(nums):
            target = target[:index[idx]]+[n]+target[index[idx]:]
        return target
        """
        for idx, n in zip(index, nums):
            target.insert(idx, n)
        return target
        """


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    print(Solution().createTargetArray(nums, index))
    nums = [1, 2, 3, 4, 0]
    index = [0, 1, 2, 3, 0]
    print(Solution().createTargetArray(nums, index))
    nums = [1]
    index = [0]
    print(Solution().createTargetArray(nums, index))
