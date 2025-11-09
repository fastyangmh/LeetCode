class Solution:
    def numDecodings(self, s: str) -> int:
        # # method1
        # n = len(s)

        # if s[0] == "0":
        #     return 0

        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1 if s[0] != "0" else 0

        # for idx in range(2, n + 1):
        #     single = s[idx - 1]
        #     double = s[idx - 2 : idx]

        #     if single != "0":
        #         dp[idx] += dp[idx - 1]

        #     if 10 <= int(double) <= 26:
        #         dp[idx] += dp[idx - 2]

        # return dp[n]

        # method2
        if s[0] == "0":
            return 0

        two_back = 1
        one_back = 1 if s[0] != "0" else 0
        curr = 0

        for idx in range(2, len(s) + 1):
            single = s[idx - 1]
            double = s[idx - 2 : idx]

            if single != "0":
                curr += one_back

            if 10 <= int(double) <= 26:
                curr += two_back

            two_back, one_back, curr = one_back, curr, 0

        return one_back
