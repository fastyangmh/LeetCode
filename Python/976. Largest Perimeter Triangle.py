#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        nums_len=len(nums)
        for idx in range(nums_len-3+1):
            array=nums[idx:idx+3]
            if len(array)==3:
                if self._check_triangle(array):
                    return sum(array)
        return 0
    
    def _check_triangle(self,array):
        s=sum(array)
        for v in array:
            if not (s-v)>v:
                return False
        return True
    
if __name__=='__main__':
    # ex1 ans 5
    nums=[2,1,2]
    print(Solution().largestPerimeter(nums=nums))
    
    # ex2 ans 0
    nums=[1,2,1]
    print(Solution().largestPerimeter(nums=nums))
    
    # ex3 ans 10
    nums=[3,2,3,4]
    print(Solution().largestPerimeter(nums=nums))
    
    # ex4 ans 8
    nums=[3,6,2,3]
    print(Solution().largestPerimeter(nums=nums))


# In[ ]:




