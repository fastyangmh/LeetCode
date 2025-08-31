class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()

        if len(pattern) != len(ss):
            return False

        map_ = {}

        for c, w in zip(pattern, ss):
            if c not in map_:
                if w in map_.values():
                    return False
                map_[c] = w
            elif map_[c] != w:
                return False

        return True
