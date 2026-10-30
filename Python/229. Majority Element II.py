class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = cand2 = None
        cnt1 = cnt2 = 0

        for x in nums:
            if x == cand1:
                cnt1 += 1
            elif x == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = x
                cnt1 += 1
            elif cnt2 == 0:
                cand2 = x
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0

        for x in nums:
            cnt1 += 1 if x == cand1 else 0
            cnt2 += 1 if x == cand2 else 0

        ans = []

        if cnt1 > len(nums) // 3:
            ans.append(cand1)

        if cnt2 > len(nums) // 3:
            ans.append(cand2)

        return ans
