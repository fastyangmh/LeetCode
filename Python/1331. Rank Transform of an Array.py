class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {v: k + 1 for k, v in enumerate(sorted(set(arr)))}

        return [rank[x] for x in arr]
