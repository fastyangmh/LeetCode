class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        l = 0

        for c in s1:
            cnt1[ord(c) - ord("a")] += 1

        for r, c in enumerate(s2):
            while r - l + 1 > len(s1):
                cnt2[ord(s2[l]) - ord("a")] -= 1
                l += 1

            cnt2[ord(c) - ord("a")] += 1

            if cnt2 == cnt1:
                return True

        return False
