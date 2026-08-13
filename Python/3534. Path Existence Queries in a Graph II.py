class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        arr = sorted([(nums[i], i) for i in range(n)])

        values = [x[0] for x in arr]

        pos = [0] * n

        for i, (_, original_i) in enumerate(arr):
            pos[original_i] = i

        component = [0] * n

        for i in range(1, n):
            component[i] = component[i - 1]

            if values[i] - values[i - 1] > maxDiff:
                component[i] += 1

        farthest = [0] * n
        r = 0

        for i in range(n):
            r = max(r, i)

            while r + 1 < n and values[r + 1] - values[i] <= maxDiff:
                r += 1

            farthest[i] = r

        LOG = max(1, n.bit_length())
        jump = [[0] * n for _ in range(LOG)]
        jump[0] = farthest[:]

        for k in range(1, LOG):
            for i in range(n):
                jump[k][i] = jump[k - 1][jump[k - 1][i]]

        ans = []

        for u, v in queries:
            left = pos[u]
            right = pos[v]

            if left > right:
                left, right = right, left

            if left == right:
                ans.append(0)
                continue

            if component[left] != component[right]:
                ans.append(-1)
                continue

            curr = left
            steps = 0

            for k in range(LOG - 1, -1, -1):
                nxt = jump[k][curr]

                if nxt < right:
                    curr = nxt
                    steps += 1 << k

            ans.append(steps + 1)

        return ans
