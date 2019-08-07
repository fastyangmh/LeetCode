class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,a in enumerate(nums):
            for j,b in enumerate(nums[i+1:]):
                if (a+b)==target:
                    return [i,i+j+1]
        return -1

if __name__ == "__main__":
    anser=Solution()
    nums=[2,7,11,15]
    target=9
    print(anser.twoSum(nums,target))