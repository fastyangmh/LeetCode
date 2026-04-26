class Solution:
    def longestBalanced(self, s: str) -> int:
        def solve(s):
            pfx_idx = {0: -1}

            freq = [0, 0]
            for c in s:
                freq[int(c)] += 1

            res = pfx = 0

            for i, c in enumerate(s):
                pfx += 1 if c == "1" else -1
                freq[int(c)] -= 1

                if pfx == 0:
                    res = max(res, i - pfx_idx[pfx])

                if freq[0] > 0 and pfx - 2 in pfx_idx:
                    res = max(res, i - pfx_idx[pfx - 2])

                if freq[1] > 0 and pfx + 2 in pfx_idx:
                    res = max(res, i - pfx_idx[pfx + 2])

                if pfx not in pfx_idx:
                    pfx_idx[pfx] = i

            return res

        return max(solve(s), solve(s[::-1]))
