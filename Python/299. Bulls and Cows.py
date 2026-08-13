from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # # method1
        # x = y = 0

        # y = sum((Counter(secret) & Counter(guess)).values())

        # for idx, ch in enumerate(secret):
        #     if guess[idx] == ch:
        #         x += 1
        #         y -= 1

        # return f"{x}A{y}B"

        # method2
        x = y = 0

        count = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                x += 1
            else:
                si = ord(s) - ord("0")
                gi = ord(g) - ord("0")

                y += 1 if count[si] < 0 else 0
                y += 1 if count[gi] > 0 else 0

                count[si] += 1
                count[gi] -= 1

        return f"{x}A{y}B"
