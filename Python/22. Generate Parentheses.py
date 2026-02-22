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

        def backtrack(s, open_cnt, close_cnt):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open_cnt < n:
                backtrack(s + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(s + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)

        return res
