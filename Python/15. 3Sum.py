from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()  # O(NlogN)
        ans = []
        for idx, v in enumerate(nums[:-2]):  # O(N**2)
            if idx >= 1 and v == nums[idx - 1]:
                continue
            v = nums[idx]
            l = idx + 1
            r = len(nums) - 1
            diff = -v
            while l < r:
                s = nums[l] + nums[r]
                if s == diff:
                    if [v, nums[l], nums[r]] not in ans:    #O(N)
                        ans.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif s > diff:
                    r -= 1
                elif s < diff:
                    l += 1
        return ans
        '''
        class Solution:
            def threeSum(self, nums: List[int]) -> List[List[int]]:
                if len(nums) < 3:
                    return []
                nums.sort()
                res = set()
                for i, v in enumerate(nums[:-2]):
                    if i >= 1 and v == nums[i-1]:
                        continue
                    d = {}
                    for x in nums[i+1:]:
                        if x not in d:
                            d[-v-x] = 1
                        else:
                            res.add((v, -v-x, x))
                return list(res)
        '''


if __name__ == '__main__':
    #ex1    [[-1,-1,2],[-1,0,1]]
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums=nums))

    #ex2    []
    nums = []
    print(Solution().threeSum(nums=nums))

    #ex3    []
    nums = [0]
    print(Solution().threeSum(nums=nums))

    #63 / 318   [[0,0,0]]
    nums = [0, 0, 0, 0]
    print(Solution().threeSum(nums=nums))

    #94 / 318   [[-2,0,2],[-2,1,1]]
    nums = [-2, 0, 1, 1, 2]
    print(Solution().threeSum(nums=nums))