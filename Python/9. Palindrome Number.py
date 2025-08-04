class Solution:
    def isPalindrome(self, x: int) -> bool:
        return int(str(x)[::-1]) == x if x >= 0 else False


if __name__ == '__main__':
    # ex1   true
    x = 121
    print(Solution().isPalindrome(x=x))

    # ex2   false
    x = -121
    print(Solution().isPalindrome(x=x))

    # ex3   false
    x = 10
    print(Solution().isPalindrome(x=x))

    # ex4   false
    x = -101
    print(Solution().isPalindrome(x=x))
