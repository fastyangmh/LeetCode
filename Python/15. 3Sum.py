class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return ans
