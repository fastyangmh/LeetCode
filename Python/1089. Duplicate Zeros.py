class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)

        if zeros == 0:
            return

        i = n - 1
        j = i + zeros

        while i >= 0:
            if arr[i] != 0:
                if j < n:
                    arr[j] = arr[i]
                j -= 1
            else:
                for _ in range(2):
                    if j < n:
                        arr[j] = 0
                    j -= 1

            i -= 1
