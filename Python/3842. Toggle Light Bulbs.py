class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        counter = {}

        for bulb in bulbs:
            counter[bulb] = counter.get(bulb, 0) + 1

        return sorted([bulb for bulb, v in counter.items() if v % 2 == 1])
