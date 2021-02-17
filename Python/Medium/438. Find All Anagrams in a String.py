from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hop = len(p)
        index = []
        for idx in range(0, len(s)-hop+1):
            t = s[idx:idx+hop]
            if all(t.count(c) == p.count(c) for c in "abcdefghijklmnopqrstuvwxyz" if c in p):
                index.append(idx)
        return index


"""
the best solution

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        result = []
        hashOfP = sum(hash(l) for l in p)
        currentHash = 0
        for l in s[:len(p)]:
            currentHash += hash(l)
        if currentHash == hashOfP: result.append(0)
        for i, l in enumerate(s[len(p):]):
            currentHash += hash(l) - hash(s[i])
            if currentHash == hashOfP:
                result.append(i+1)
        return result
"""

if __name__ == "__main__":
    # ex1   [0,6]
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s=s, p=p))
    # ex2   [0,1,2]
    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s=s, p=p))
