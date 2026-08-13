class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(distance):
            last = position[0]
            count = 1

            for idx in range(1, len(position)):
                curr = position[idx]

                if curr - last >= distance:
                    last = curr
                    count += 1

            return count >= m

        left, right = 1, position[-1] - position[0]

        while left < right:
            mid = (left + right + 1) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left
