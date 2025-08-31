class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_ = {}

        for c in s:
            map_[c] = map_.get(c, 0) + 1

        for idx, c in enumerate(s):
            if map_[c] == 1:
                return idx

        return -1
