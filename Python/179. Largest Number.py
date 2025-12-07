from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # method1
        nums_str = list(map(str, nums))
        nums_str = sorted(nums_str, key=lambda x: x * 10, reverse=True)

        if nums_str[0] == "0":
            return "0"

        return "".join(nums_str)

        # # method2
        # def compare_func(a, b):
        #     if a + b > b + a:
        #         return -1
        #     elif a + b < b + a:
        #         return 1
        #     else:
        #         return 0

        # nums_str = list(map(str, nums))
        # nums_str = sorted(nums_str, key=cmp_to_key(compare_func))

        # if nums_str[0] == "0":
        #     return "0"

        # return "".join(nums_str)
