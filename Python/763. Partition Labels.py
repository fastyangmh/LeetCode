class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for idx, ch in enumerate(s):
            last[ch] = idx

        start = end = 0
        ans = []

        for idx, ch in enumerate(s):
            end = max(end, last[ch])

            if idx == end:
                ans.append(end - start + 1)
                start = idx + 1

        return ans
