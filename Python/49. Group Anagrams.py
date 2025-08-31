from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = {}

        for word in strs:
            chr_arr = [0] * 26

            for c in word:
                chr_arr[ord(c) - ord("a")] += 1

            map_.setdefault(tuple(chr_arr), []).append(word)

        return list(map_.values())
