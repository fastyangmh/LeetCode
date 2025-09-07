from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # # method1
        # res = []

        # def is_valid(comb):
        #     stack = []

        #     for p in "".join(comb):
        #         if p == "(":
        #             stack.append(p)
        #         else:
        #             if not stack:
        #                 return False
        #             if stack.pop() + p != "()":
        #                 return False

        #     return not stack

        # def helper(comb):
        #     if len(comb) == n * 2:
        #         if not is_valid(comb):
        #             return

        #         res.append("".join(comb))
        #         return

        #     for p in ("(", ")"):
        #         comb.append(p)
        #         helper(comb)
        #         comb.pop()

        # helper([])

        # return res

        # method2
        res = []

        def backtrack(path, left, right):
            if len(path) == 2 * n:
                res.append("".join(path))

            if left < n:
                path.append("(")
                backtrack(path, left + 1, right)
                path.pop()

            if right < left:
                path.append(")")
                backtrack(path, left, right + 1)
                path.pop()

        backtrack([], 0, 0)

        return res
