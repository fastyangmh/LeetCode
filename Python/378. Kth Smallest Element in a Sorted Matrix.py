import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # # method1
        # n = len(matrix)
        # heap = []

        # for r in range(n):
        #     heapq.heappush(heap, (matrix[r][0], r, 0))

        # for _ in range(k - 1):
        #     val, r, c = heapq.heappop(heap)

        #     if c + 1 < n:
        #         heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

        # return heapq.heappop(heap)[0]

        # method2
        n = len(matrix)

        def count_less_equal(x):
            r, c = 0, n - 1
            count = 0

            while r < n and c >= 0:
                if matrix[r][c] > x:
                    c -= 1
                else:
                    count += c + 1
                    r += 1

            return count

        lo, hi = matrix[0][0], matrix[-1][-1]

        while lo < hi:
            mid = (lo + hi) // 2

            if count_less_equal(mid) < k:
                lo = mid + 1
            else:
                hi = mid

        return lo
