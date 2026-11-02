class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}

        for s in strs:
            chars = [0] * 26

            for c in s:
                chars[ord(c) - ord("a")] += 1

            seen.setdefault(tuple(chars), []).append(s)

        return list(seen.values())
