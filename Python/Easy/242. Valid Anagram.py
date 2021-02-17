from numpy.lib.twodim_base import mask_indices


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict, tDict = {}, {}
        for sV, tV in zip(s, t):
            if sDict.get(sV):
                sDict[sV] += 1
            else:
                sDict[sV] = 1
            if tDict.get(tV):
                tDict[tV] += 1
            else:
                tDict[tV] = 1
        return True if sDict == tDict else False


"""
the best solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all(s.count(c) == t.count(c) for c in "abcdefghijklmnopqrstuvwxyz")
"""

if __name__ == "__main__":
    # ex1    true
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s=s, t=t))

    # ex2    false
    s = "rat"
    t = "car"
    print(Solution().isAnagram(s=s, t=t))

    # 26/34  false
    s = "a"
    t = "ab"
    print(Solution().isAnagram(s=s, t=t))

    # 31/35  false
    s = "aacc"
    t = "ccac"
    print(Solution().isAnagram(s=s, t=t))
