class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):
            if s_to_t.get(c1, c2) != c2:
                return False
            if t_to_s.get(c2, c1) != c1:
                return False

            s_to_t[c1] = c2
            t_to_s[c2] = c1

        return True
