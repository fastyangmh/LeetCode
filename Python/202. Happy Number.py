class Solution:
    def isHappy(self, n: int) -> bool:
        # # method1
        # def get_next_n(n):
        #     ret = 0

        #     while n:
        #         ret += (n % 10) ** 2
        #         n //= 10

        #     return ret

        # seen = set()

        # while n not in seen:
        #     seen.add(n)
        #     n = get_next_n(n)

        #     if n == 1:
        #         return True

        # return False

        # method2
        def get_next_n(n):
            ret = 0

            while n:
                ret += (n % 10) ** 2
                n //= 10

            return ret

        slow = n
        fast = get_next_n(slow)

        while fast != 1 and slow != fast:
            slow = get_next_n(slow)
            fast = get_next_n(get_next_n(fast))

        return fast == 1
