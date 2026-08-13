import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for u, v, w in times:
            graph.setdefault(u, []).append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        pq = [(0, k)]

        while pq:
            curr_dist, node = heapq.heappop(pq)

            if curr_dist > dist[node]:
                continue

            for nxt, weight in graph.get(node, []):
                new_dist = curr_dist + weight

                if new_dist < dist[nxt]:
                    dist[nxt] = new_dist
                    heapq.heappush(pq, (new_dist, nxt))

        ans = max(dist[1:])

        return ans if ans != float("inf") else -1
