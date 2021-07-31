from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_table = {}
        for v in arr:
            if 2*v in hash_table or (v % 2 == 0 and v//2 in hash_table):
                return True
            hash_table[v] = None
        return False


if __name__ == '__main__':
    # ex1    ans true
    arr = [10, 2, 5, 3]
    print(Solution().checkIfExist(arr=arr))

    # ex2    ans true
    arr = [7, 1, 14, 11]
    print(Solution().checkIfExist(arr=arr))

    # ex3    ans false
    arr = [3, 1, 7, 11]
    print(Solution().checkIfExist(arr=arr))
