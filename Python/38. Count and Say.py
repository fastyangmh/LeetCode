class Solution:
    def countAndSay(self, n: int) -> str:
        # method1
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)

        parts = []
        i = 0

        while i < len(prev):
            j = i
            count = 0

            while j < len(prev) and prev[j] == prev[i]:
                count += 1
                j += 1

            parts.append(f"{count}{prev[i]}")
            i = j

        return "".join(parts)

        # # method2
        # prev = "1"

        # for _ in range(1, n):
        #     parts = []
        #     i = 0

        #     while i < len(prev):
        #         j = i
        #         count = 0

        #         while j < len(prev) and prev[j] == prev[i]:
        #             count += 1
        #             j += 1

        #         parts.append(f"{count}{prev[i]}")
        #         i = j

        #     prev = "".join(parts)

        # return prev
