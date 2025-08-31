class Solution:
    def reverseBits(self, n: int) -> int:
        # method1
        bits = 32
        ans = 0

        for idx in range(bits):
            ans += (1 << (bits - 1 - idx)) * (n & 1)  # minus 1 because bits is 0 ~ 31, ex, idx = 0, bits - idx = 32, will error
            n >>= 1

        return ans

        # # method2
        # bits = 32
        # ans = 0

        # for _ in range(bits):
        #     ans = (ans << 1) | (n & 1)
        #     n >>= 1

        # return ans
