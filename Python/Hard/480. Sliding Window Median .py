from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        array = nums[:k]
        ans = [self.median(array=sorted(array))]
        for idx in range(k, len(nums)):
            array.pop(0)
            array.append(nums[idx])
            ans.append(self.median(array=sorted(array)))
        return ans

    def median(self, array):
        n = len(array)
        if n % 2 == 0:
            idx = n//2
            return (array[idx-1]+array[idx])/2
        else:
            return array[n//2]


if __name__ == '__main__':
    # ex1    ans [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().medianSlidingWindow(nums=nums, k=k))

    # ex2    ans [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k = 3
    print(Solution().medianSlidingWindow(nums=nums, k=k))
