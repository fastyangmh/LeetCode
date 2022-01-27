from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for v in accounts:
            ans = max(ans, sum(v))
        return ans


if __name__ == '__main__':
    #ex1    ans:    6
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(Solution().maximumWealth(accounts=accounts))

    #ex2    ans:    10
    accounts = [[1, 5], [7, 3], [3, 5]]
    print(Solution().maximumWealth(accounts=accounts))

    #ex3    ans:    17
    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    print(Solution().maximumWealth(accounts=accounts))
