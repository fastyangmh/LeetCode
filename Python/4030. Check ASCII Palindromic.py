class Solution:
    def isPalindromic(self, s: str) -> bool:
        n = len(s)
        total_bits = 8 * n

        for left in range(total_bits // 2):
            right = total_bits - 1 - left

            left_char = left // 8
            left_bit = 7 - (left % 8)

            right_char = right // 8
            right_bit = 7 - (right % 8)

            bit1 = (ord(s[left_char]) >> left_bit) & 1
            bit2 = (ord(s[right_char]) >> right_bit) & 1

            if bit1 != bit2:
                return False

        return True
