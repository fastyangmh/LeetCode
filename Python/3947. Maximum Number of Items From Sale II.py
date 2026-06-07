class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        count_factor = [0] * (n + 1)
        cheapest_price = float("inf")

        for factor, price in items:
            count_factor[factor] += 1
            cheapest_price = min(cheapest_price, price)

        free_limit = [0] * (n + 1)

        for f in range(1, n + 1):
            if count_factor[f] == 0:
                continue

            total_multiples = 0

            for multiple in range(f, n + 1, f):
                total_multiples += count_factor[multiple]

            free_limit[f] = total_multiples - 1

        bonus_deals = []
        threshold = cheapest_price * 2

        for factor, price in items:
            if price >= threshold:
                continue

            bonus_count = free_limit[factor]

            if bonus_count > 0:
                bonus_deals.append([price, bonus_count])

        bonus_deals.sort()
        total_items = 0

        for price, max_bonus_copies in bonus_deals:
            if budget < price:
                break

            buy_count = min(max_bonus_copies, budget // price)
            budget -= price * buy_count
            total_items += buy_count * 2

        total_items += budget // cheapest_price

        return total_items
