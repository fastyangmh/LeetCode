from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for i in range(n):
            discount = 0
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    discount += prices[j]
                    break
            prices[i] -= discount
        return prices


'''
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [0]*len(prices)
        stack = []
        for i, price in enumerate(prices):
            while stack and price <= stack[-1][0]:
                old_price, idx = stack.pop()
                ans[idx] = old_price-price
            stack.append((price, i))
        for (price, idx) in stack:
            ans[idx] = price
        return ans
'''


if __name__ == '__main__':
    # ex1   ans [4,2,4,2,3]
    prices = [8, 4, 6, 2, 3]
    print(Solution().finalPrices(prices=prices))

    # ex2    ans [1,2,3,4,5]
    prices = [1, 2, 3, 4, 5]
    print(Solution().finalPrices(prices=prices))

    # ex3    ans [9,0,1,6]
    prices = [10, 1, 1, 6]
    print(Solution().finalPrices(prices=prices))
