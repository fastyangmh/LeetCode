class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # # method1
        # ans = []
        # digits = "123456789"

        # low_len = len(str(low))
        # high_len = len(str(high))

        # for length in range(low_len, high_len + 1):
        #     for start in range(len(digits) - length + 1):
        #         num = int(digits[start : start + length])

        #         if low <= num <= high:
        #             ans.append(num)

        # return ans

        # method2
        low_len = len(str(low))
        high_len = len(str(high))
        ans = []

        for length in range(low_len, high_len + 1):
            for start in range(1, 10 - length + 1):
                num = 0

                for digit in range(start, start + length):
                    num = num * 10 + digit

                if low <= num <= high:
                    ans.append(num)

        return ans
