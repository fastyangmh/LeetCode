class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for idx in range(len(s)):
            l = s[:idx]
            r = s[idx:]
            if r+l == goal:
                return True
        return False


if __name__ == '__main__':
    # ex1    ans true
    s = "abcde"
    goal = "cdeab"
    print(Solution().rotateString(s=s, goal=goal))

    # ex2    ans false
    s = "abcde"
    goal = "abced"
    print(Solution().rotateString(s=s, goal=goal))
