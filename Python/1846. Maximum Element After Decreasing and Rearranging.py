class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # # method1
        # arr.sort()
        # arr[0] = 1

        # for i in range(1, len(arr)):
        #     arr[i] = min(arr[i], arr[i - 1] + 1)

        # return arr[-1]

        # method2
        arr.sort()
        ans = 1

        for num in arr:
            if num >= ans:
                ans += 1

        return ans - 1
