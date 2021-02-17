class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            cumsum = 0
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = 1
                    cumsum += 1
                else:
                    cumsum += dp[i-1][j]
                    if j-i >= 0:    # basically sliding window
                        cumsum -= dp[i-1][j-i]
                    dp[i][j] = cumsum % 1000000007
        return dp[n][k]


if __name__ == "__main__":
    # example 1
    n = 3
    k = 0
    print(Solution().kInversePairs(n=n, k=k))  # 1

    # example 2
    n = 3
    k = 1
    print(Solution().kInversePairs(n=n, k=k))  # 2

    # 12/80
    n = 10
    k = 1
    print(Solution().kInversePairs(n=n, k=k))  # 9

    # 13/80
    n = 10
    k = 2
    print(Solution().kInversePairs(n=n, k=k))  # 44

    # 14/80
    n = 10
    k = 3
    print(Solution().kInversePairs(n=n, k=k))  # 155

    # 15/80
    n = 10
    k = 4
    print(Solution().kInversePairs(n=n, k=k))  # 440
