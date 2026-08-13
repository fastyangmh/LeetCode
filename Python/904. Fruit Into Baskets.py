class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = {}
        ans = 0
        left = 0

        for right, x in enumerate(fruits):
            seen[x] = seen.get(x, 0) + 1

            while len(seen) > 2:
                left_most = fruits[left]
                seen[left_most] -= 1

                if seen[left_most] == 0:
                    del seen[left_most]

                left += 1

            ans = max(ans, right - left + 1)

        return ans
