class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []

        def backtrack(pos, cost, prev_one, path):
            if pos == n:
                ans.append("".join(path))
                return

            # 0
            backtrack(pos + 1, cost, False, path + ["0"])

            # 1
            if not prev_one and cost + pos <= k:
                backtrack(pos + 1, cost + pos, True, path + ["1"])

        backtrack(0, 0, False, [])

        return ans
