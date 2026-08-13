class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(amount):
            children = 0

            for c in candies:
                children += c // amount

            return children >= k

        left, right = 0, max(candies)

        while left < right:
            mid = (left + right + 1) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left
