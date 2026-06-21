class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        square_sum = 0
        digit_sum = 0

        while n > 0:
            num = n % 10
            n //= 10

            square_sum += num**2
            digit_sum += num

        return square_sum - digit_sum >= 50
