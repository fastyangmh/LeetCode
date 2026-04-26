class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # # method1
        # groups = []
        # curr = 1

        # for i in range(1, len(s)):
        #     if s[i] == s[i - 1]:
        #         curr += 1
        #     else:
        #         groups.append(curr)
        #         curr = 1

        # groups.append(curr)

        # ans = 0

        # for i in range(len(groups)):
        #     prev = groups[i - 1] if i > 0 else 0
        #     curr = groups[i]

        #     ans += min(prev, curr)

        # return ans

        # method2
        prev, curr = 0, 1
        ans = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1

        ans += min(prev, curr)

        return ans
