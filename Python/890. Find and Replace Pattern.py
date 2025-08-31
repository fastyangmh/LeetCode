from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []

        for w in words:
            map_ = {}
            is_bijection = True

            for cw, cp in zip(w, pattern):
                if cw not in map_:
                    if cp in map_.values():
                        is_bijection = False
                        break
                    map_[cw] = cp
                elif map_[cw] != cp:
                    is_bijection = False
                    break

            if is_bijection:
                ans.append(w)

        return ans
