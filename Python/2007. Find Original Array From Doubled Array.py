from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)

        if n % 2:
            return []

        changed.sort()
        counter = Counter(changed)
        ans = []

        for num in changed:
            if counter[num] == 0:
                continue

            if counter[2 * num] == 0:
                return []

            counter[num] -= 1
            counter[2 * num] -= 1
            ans.append(num)

        return ans
