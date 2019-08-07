class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        n = x
        if n < 0:
            return False
        while n > 0:
            y = y*10+n % 10
            n //= 10
        return True if y == x else False


if __name__ == "__main__":
    x = -121
    print(Solution().isPalindrome(x))
