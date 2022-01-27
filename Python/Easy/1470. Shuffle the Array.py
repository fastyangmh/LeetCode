from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        ans = []
        while True:
            if i == n:
                break
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j += 1
        return ans
        '''
        fastest solution
        res = []
        for i, j in zip(nums[:n], nums[n:]):
            res += [i, j]
        return res
        '''


if __name__ == '__main__':
    #ex1    ans:    [2,3,5,4,1,7]
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(Solution().shuffle(nums=nums, n=n))

    #ex2    ans:    [1,4,2,3,3,2,4,1]
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(Solution().shuffle(nums=nums, n=n))

    #ex3    ans:    [1,2,1,2]
    nums = [1, 1, 2, 2]
    n = 2
    print(Solution().shuffle(nums=nums, n=n))
