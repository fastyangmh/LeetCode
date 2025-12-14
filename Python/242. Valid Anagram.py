class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method1
        if len(s) != len(t):
            return False

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for c in t:
            if c not in freq or freq[c] <= 0:
                return False
            freq[c] -= 1

        return True

        # # method2
        # if len(s) != len(t):
        #     return False

        # def count(words):
        #     results = {}

        #     for c in words:
        #         results[c] = results.get(c, 0) + 1

        #     return results

        # counter_s = count(s)
        # counter_t = count(t)

        # return counter_s == counter_t
