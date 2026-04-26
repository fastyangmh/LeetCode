class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # # method1 brute
        # for i in range(len(s)):
        #     if s[i:] + s[:i] == goal:
        #         return True

        # return False

        # method2
        return goal in s + s if len(s) == len(goal) else False
