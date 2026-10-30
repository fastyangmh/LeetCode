class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            takes = 1
            curr = 0

            for weight in weights:
                if curr + weight > capacity:
                    takes += 1
                    curr = weight
                else:
                    curr += weight

            return takes <= days

        l, r = max(weights), sum(weights)

        while l < r:
            capacity = (l + r) // 2

            if check(capacity):
                r = capacity
            else:
                l = capacity + 1

        return l
