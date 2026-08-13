class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # # method1
        # ans = 0

        # for bit in range(32):
        #     bit_count = 0

        #     for x in nums:
        #         bit_count += x >> bit & 1

        #     if bit_count % 3:
        #         ans |= 1 << bit

        # if ans > 2**31 - 1:
        #     ans -= 2**32

        # return ans

        # method2
        ones = twos = 0

        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones

        return ones
