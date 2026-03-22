class Solution:
    def countCommas(self, n: int) -> int:
        return max(
            0, n - 999
        )  # 1 <= n <= 10**5 so that commas just 1 in this interval for each number
