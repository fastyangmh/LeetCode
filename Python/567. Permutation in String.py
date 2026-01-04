class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt1 = [0] * 26
        cnt2 = [0] * 26
        left = 0

        for ch in s1:
            cnt1[ord(ch) - ord("a")] += 1

        for right, ch in enumerate(s2):
            cnt2[ord(ch) - ord("a")] += 1

            if right - left + 1 > len(s1):
                cnt2[ord(s2[left]) - ord("a")] -= 1
                left += 1

            if cnt1 == cnt2:
                return True

        return False
