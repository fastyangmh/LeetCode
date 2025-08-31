class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # char_map = {}

        # for sc, tc in zip(s, t):
        #     if sc not in char_map:
        #         if tc in char_map.values():
        #             return False
        #         char_map[sc] = tc
        #     elif char_map[sc] != tc:
        #         return False

        # return True

        char_index_s = {}
        char_index_t = {}

        for idx, (sc, tc) in enumerate(zip(s, t)):
            if sc not in char_index_s:
                char_index_s[sc] = idx

            if tc not in char_index_t:
                char_index_t[tc] = idx

            if char_index_s[sc] != char_index_t[tc]:
                return False

        return True
