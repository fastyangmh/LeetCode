class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            sign = -1
            x *= sign
        else:
            sign = 1
        array = []
        while x != 0:
            array.append(str(x % 10))
            x = x//10

        number = int(''.join(array))*sign

        if number < (-2**31) or number > (2**31)-1:
            return 0
        else:
            return number


if __name__ == '__main__':
    # ex1    321
    x = 123
    print(Solution().reverse(x=x))

    # ex2   -321
    x = -123
    print(Solution().reverse(x=x))

    # ex3   21
    x = 120
    print(Solution().reverse(x=x))

    # ex4   0
    x = 0
    print(Solution().reverse(x=x))
