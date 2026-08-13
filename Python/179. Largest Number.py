from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # # method1
        # strs = list(map(str, nums))

        # def compare(a, b):
        #     if a + b > b + a:
        #         return -1
        #     elif a + b < b + a:
        #         return 1
        #     else:
        #         return 0

        # strs.sort(key=cmp_to_key(compare))

        # if strs[0] == "0":
        #     return "0"

        # return "".join(strs)

        # method2
        strs = list(map(str, nums))
        strs.sort(key=lambda x: x * 10, reverse=True)

        if strs[0] == "0":
            return "0"

        return "".join(strs)
