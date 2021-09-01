from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # time O(n) space O(n)

        hash_table = {}
        for v in arr:
            hash_table[v] = None

        count = 0
        missing_value = 1
        while True:
            if missing_value not in hash_table:
                count += 1
            if count == k:
                break
            missing_value += 1
        return missing_value

        '''
        # time O(n) space O(1)
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l+(r-l)//2
            if arr[mid]-(mid+1) >= k:
                r = mid-1
            else:
                l = mid+1
        return arr[r]+k-(arr[r]-(r+1))
        '''


if __name__ == '__main__':
    # ex1    ans    9
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(Solution().findKthPositive(arr=arr, k=k))

    # ex2    ans 6
    arr = [1, 2, 3, 4]
    k = 2
    print(Solution().findKthPositive(arr=arr, k=k))
