class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            cnt = [0] * 26

            for c in s:
                i = ord(c) - ord("a")
                cnt[i] += 1

            key = tuple(cnt)
            groups.setdefault(key, []).append(s)

        return list(groups.values())
