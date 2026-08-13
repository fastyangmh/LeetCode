from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # # method1
        # sorted_unique = sorted(set(nums))
        # ranks = {v: i + 1 for i, v in enumerate(sorted_unique)}

        # size = len(ranks) + 1
        # tree = [0] * (size + 1)

        # def update(i):
        #     while i < len(tree):
        #         tree[i] += 1
        #         i += i & -i

        # def query(i):
        #     s = 0

        #     while i > 0:
        #         s += tree[i]
        #         i -= i & -i

        #     return s

        # result = []

        # for n in reversed(nums):
        #     rank = ranks[n]
        #     result.append(query(rank - 1))
        #     update(rank)

        # return result[::-1]

        # method2
        n = len(nums)
        ans = [0] * n
        arr = [(v, i) for i, v in enumerate(nums)]

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid, right)

            right_smaller = 0
            merged = []
            i, j = left, mid

            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    ans[arr[i][1]] += right_smaller
                    merged.append(arr[i])
                    i += 1
                else:
                    right_smaller += 1
                    merged.append(arr[j])
                    j += 1

            while i < mid:
                ans[arr[i][1]] += right_smaller
                merged.append(arr[i])
                i += 1

            while j < right:
                merged.append(arr[j])
                j += 1

            arr[left:right] = merged

            return

        merge_sort(0, n)
        return ans
