from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # method1
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def helper(idx, comb):
            if idx == len(digits):
                res.append("".join(comb))
                return

            for letter in digit_to_letters[digits[idx]]:
                comb.append(letter)
                helper(idx + 1, comb)
                comb.pop()

        helper(0, [])

        return res

        # # method2
        # if not digits:
        #     return []

        # digit_to_letters = {
        #     "2": "abc",
        #     "3": "def",
        #     "4": "ghi",
        #     "5": "jkl",
        #     "6": "mno",
        #     "7": "pqrs",
        #     "8": "tuv",
        #     "9": "wxyz",
        # }
        # res = []
        # queue = [""]

        # for d in digits:
        #     for _ in range(len(queue)):
        #         prefix = queue.pop(0)

        #         for letter in digit_to_letters[d]:
        #             queue.append(prefix + letter)

        # return queue
