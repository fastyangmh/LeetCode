class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(substring):
            l, r = 0, len(substring) - 1

            while l <= r:
                if substring[l] != substring[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()

        backtrack(0)

        return res
