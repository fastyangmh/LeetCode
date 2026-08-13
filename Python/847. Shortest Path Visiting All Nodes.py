class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque()
        visited = set()
        target = (1 << n) - 1

        for i in range(n):
            queue.append((i, 1 << i))
            visited.add(queue[-1])

        dist = 0

        while queue:
            for _ in range(len(queue)):
                node, mask = queue.popleft()

                if mask == target:
                    return dist

                for next_node in graph[node]:
                    new_mask = mask | 1 << next_node
                    state = (next_node, new_mask)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            dist += 1

        return -1
