from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key=lambda x: abs(x))
        counter = Counter(arr)

        for num in arr:
            if counter[num] == 0:
                continue

            if counter[2 * num] == 0:
                return False

            counter[num] -= 1
            counter[2 * num] -= 1

        return True
