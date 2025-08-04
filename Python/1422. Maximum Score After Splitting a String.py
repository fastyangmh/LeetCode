class Solution:
    def maxScore(self, s: str) -> int:
        # time O(n^2) space O(1)
        ans = 0
        for idx in range(1, len(s)):
            left = s[:idx]
            right = s[idx:]
            reuslt = left.count('0')+right.count('1')
            if reuslt > ans:
                ans = reuslt
        return ans


if __name__ == '__main__':
    # ex1    ans    5
    s = "011101"
    print(Solution().maxScore(s=s))

    # ex2    ans 5
    s = "00111"
    print(Solution().maxScore(s=s))

    # ex3    ans 3
    s = "1111"
    print(Solution().maxScore(s=s))
