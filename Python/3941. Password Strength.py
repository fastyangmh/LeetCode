class Solution:
    def passwordStrength(self, password: str) -> int:
        ans = 0

        for s in set(password):
            if s.islower():
                ans += 1
            elif s.isupper():
                ans += 2
            elif s.isdigit():
                ans += 3
            else:
                ans += 5

        return ans
