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
        res = [0] * n
        enum = list(enumerate(nums))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    res[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                res[left[i][0]] += j
                merged.append(left[i])
                i += 1

            merged += right[j:]

            return merged

        merge_sort(enum)

        return res
