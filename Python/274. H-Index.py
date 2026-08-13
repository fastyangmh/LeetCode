class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # # method1 time: O(n log n), space: O(1)
        # left, right = 0, len(citations)

        # while left < right:
        #     h_index = (left + right + 1) // 2

        #     papers = sum(c >= h_index for c in citations)

        #     if papers >= h_index:
        #         left = h_index
        #     else:
        #         right = h_index - 1

        # return left

        # # method2 time: O(n log n), space: O(1)
        # citations.sort(reverse=True)

        # h_index = 0

        # for idx, citation in enumerate(citations):
        #     if citation >= idx + 1:
        #         h_index = idx + 1
        #     else:
        #         break

        # return h_index

        # method3 time: O(n), space: O(n)
        n = len(citations)
        count = [0] * (n + 1)

        for c in citations:
            count[min(c, n)] += 1

        papers = 0

        for h_index in range(n, -1, -1):
            papers += count[h_index]

            if papers >= h_index:
                return h_index

        return 0
