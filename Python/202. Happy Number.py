class Solution:
    def isHappy(self, n: int) -> bool:
        def squares_digits(n):
            s = 0

            while n > 0:
                s += (n % 10) ** 2
                n //= 10

            return s

        slow = n
        fast = squares_digits(n)

        while fast != 1 and slow != fast:
            slow = squares_digits(slow)
            fast = squares_digits(squares_digits(fast))

        return fast == 1
