from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        left = []
        middle = ""

        for i in range(ord("a"), ord("z") + 1):
            char = chr(i)
            cnt = count[char]

            left.append(char * (cnt // 2))

            if cnt % 2 == 1:
                middle = char

        left = "".join(left)
        right = left[::-1]

        return left + middle + right
