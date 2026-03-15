class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        min_cap = float("inf")
        ans = -1

        for i, c in enumerate(capacity):
            if c >= itemSize and c < min_cap:
                min_cap = c
                ans = i

        return ans
