class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(is_left):
            l, r = 0, len(nums) - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    ans = mid

                    if is_left:
                        r = mid - 1
                    else:
                        l = mid + 1

            return ans

        return [bs(True), bs(False)]
