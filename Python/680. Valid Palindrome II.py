class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s): return s == s[::-1]
        n = len(s)
        for idx in range(n//2):
            if s[idx] != s[n-1-idx]:
                return check(s[idx:n-1-idx]) or check(s[idx+1:n-1-idx+1])
        return True


if __name__ == '__main__':
    # ex1    ans true
    s = "aba"
    print(Solution().validPalindrome(s=s))

    # ex2    ans true
    s = "abca"
    print(Solution().validPalindrome(s=s))

    # ex3    ans false
    s = "abc"
    print(Solution().validPalindrome(s=s))

    # 347/467    ans false
    s = "tebbem"
    print(Solution().validPalindrome(s=s))
