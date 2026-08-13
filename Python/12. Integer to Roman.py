class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        ans = []

        remaining = num

        for value, symbol in symbols:
            if value > remaining:
                continue

            count = remaining // value
            ans.append(symbol * count)
            remaining -= value * count

        return "".join(ans)
