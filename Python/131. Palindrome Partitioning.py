class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        ans = []

        def backtrack(start, path):
            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start : end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])

        return ans
