class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        # # method1
        # n = len(nums)
        # seen = {}
        # distinct = 0
        # i = 0

        # while i < n:
        #     j = i

        #     while j < n and nums[j] == nums[i]:
        #         j += 1

        #     if nums[i] not in seen:
        #         distinct += 1
        #     elif seen[nums[i]] == 1:
        #         distinct -= 1

        #     seen[nums[i]] = seen.get(nums[i], 0) + 1

        #     i = j

        # return distinct

        # method2
        seen = set()
        non_special = set()

        for i, x in enumerate(nums):
            if i == 0 or x != nums[i - 1]:
                if x in seen:
                    non_special.add(x)
                else:
                    seen.add(x)

        return len(seen) - len(non_special)
