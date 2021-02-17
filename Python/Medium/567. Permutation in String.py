class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hop = len(s1)
        for idx in range(0, len(s2)-hop+1):
            t = s2[idx:idx+hop]
            if all(t.count(c) == s1.count(c) for c in "abcdefghijklmnopqrstuvwxyz" if c in s1):
                return True
        return False


"""
inspire by 438 the best solution

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hop = len(s1)
        s1Hash = sum(hash(v) for v in s1)
        currentHash = sum(hash(v) for v in s2[:hop])
        if currentHash == s1Hash:
            return True
        for idx, v in enumerate(s2[hop:]):
            currentHash+=hash(v)-hash(s2[idx])
            if currentHash == s1Hash:
                return True
        return False
"""


if __name__ == "__main__":
    # ex1    true
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1=s1, s2=s2))

    # ex2    false
    s1 = "ab"
    s2 = "eidboaoo"
    print(Solution().checkInclusion(s1=s1, s2=s2))
