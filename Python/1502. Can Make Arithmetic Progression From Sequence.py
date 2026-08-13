class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[0] - arr[1]

        for i in range(1, len(arr) - 1):
            curr = arr[i] - arr[i + 1]
            if curr != diff:
                return False

        return True
