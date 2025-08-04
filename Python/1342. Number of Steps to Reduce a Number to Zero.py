class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if not num % 2:
                num /= 2
            else:
                num -= 1
            step += 1
        return step


if __name__ == "__main__":
    num = 14
    print(Solution().numberOfSteps(num))
    num = 8
    print(Solution().numberOfSteps(num))
    num = 123
    print(Solution().numberOfSteps(num))
