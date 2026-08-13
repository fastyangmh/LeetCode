class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(open_count, close_count, path):
            if open_count + close_count == 2 * n:
                ans.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count, path)
                path.pop()

            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1, path)
                path.pop()

        backtrack(0, 0, [])

        return ans
