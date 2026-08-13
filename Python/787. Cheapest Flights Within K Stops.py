class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        INF = float("inf")

        cost = [INF] * n
        cost[src] = 0

        for _ in range(k + 1):
            next_cost = cost[:]

            for u, v, p in flights:
                if cost[u] == INF:
                    continue

                next_cost[v] = min(next_cost[v], cost[u] + p)

            cost = next_cost

        return cost[dst] if cost[dst] != INF else -1
