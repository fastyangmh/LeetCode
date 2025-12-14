from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # method1
        # seen = {}

        # for word in strs:
        #     key = "".join(sorted(word))
        #     seen.setdefault(key, []).append(word)

        # return list(seen.values())

        # method2
        seen = {}

        for word in strs:
            chrs = [0] * 26

            for c in word:
                chrs[ord(c) - ord("a")] += 1

            seen.setdefault(tuple(chrs), []).append(word)

        return list(seen.values())
