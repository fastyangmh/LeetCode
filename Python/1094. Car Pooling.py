class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001

        for x, start, end in trips:
            diff[start] += x
            diff[end] -= x

        curr = 0

        for v in diff:
            curr += v

            if curr > capacity:
                return False

        return True
