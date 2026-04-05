class Solution:
    def numDecodings(self, s: str) -> int:
        # # method1
        # if s[0] == "0":
        #     return 0

        # n = len(s)

        # dp = [0] * (n + 1)
        # dp[0] = dp[1] = 1

        # for idx in range(2, n + 1):
        #     single = s[idx - 1]
        #     double = s[idx - 2 : idx]

        #     if single != "0":
        #         dp[idx] += dp[idx - 1]

        #     if 10 <= int(double) <= 26:
        #         dp[idx] += dp[idx - 2]

        # return dp[-1]

        # method2
        if s[0] == "0":
            return 0

        prev2 = prev1 = 1

        for i in range(2, len(s) + 1):
            curr = 0

            if s[i - 1] != "0":
                curr += prev1

            if 10 <= int(s[i - 2 : i]) <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1
