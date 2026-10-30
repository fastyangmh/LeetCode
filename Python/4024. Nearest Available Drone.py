class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        minimum = float("inf")
        ans = -1

        for i, (x, y, r) in enumerate(drones):
            distance = abs(x - target[0]) + abs(y - target[1])

            if distance <= r and distance < minimum:
                minimum = distance
                ans = i

        return ans
