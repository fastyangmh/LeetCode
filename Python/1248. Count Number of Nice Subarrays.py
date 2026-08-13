class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # # method1
        # count = {0: 1}
        # prefix = 0
        # ans = 0

        # for x in nums:
        #     prefix += 1 if x & 1 else 0

        #     diff = prefix - k

        #     ans += count.get(diff, 0)

        #     count[prefix] = count.get(prefix, 0) + 1

        # return ans

        # method2
        def count_at_most(k):
            if k < 0:
                return 0

            left = 0
            ret = 0
            count = 0

            for right, x in enumerate(nums):
                count += 1 if x & 1 else 0

                while count > k:
                    count -= 1 if nums[left] & 1 else 0
                    left += 1
                ret += right - left + 1

            return ret

        return count_at_most(k) - count_at_most(k - 1)
