class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        combs = {}
        limit = int(n ** (1 / 3))

        for i in range(1, limit + 1):
            a = i**3

            for j in range(i, limit + 1):
                b = j**3

                s = a + b

                if s > n:
                    break

                combs[s] = combs.get(s, 0) + 1

        ans = [k for k, v in combs.items() if v > 1]
        ans.sort()

        return ans
