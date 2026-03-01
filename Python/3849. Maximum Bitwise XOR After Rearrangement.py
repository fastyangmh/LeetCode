class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        ones = t.count("1")
        zeros = len(t) - ones
        n = ""

        for ch in s:
            if ch == "1":
                if zeros > 0:
                    n += "1"
                    zeros -= 1
                else:
                    n += "0"
                    ones -= 1
            elif ch == "0":
                if ones > 0:
                    n += "1"
                    ones -= 1
                else:
                    n += "0"
                    zeros -= 1

        return n
