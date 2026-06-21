class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            cnt = {}
            freq_cnt = {}
            distinct = 0

            for j in range(i, n):
                x = nums[j]

                old = cnt.get(x, 0)

                if old > 0:
                    freq_cnt[old] -= 1

                    if freq_cnt[old] == 0:
                        del freq_cnt[old]
                else:
                    distinct += 1

                new = old + 1
                cnt[x] = new
                freq_cnt[new] = freq_cnt.get(new, 0) + 1

                length = j - i + 1

                if distinct == 1:
                    ans = max(ans, length)
                elif len(freq_cnt) == 2:
                    a, b = sorted(freq_cnt.keys())

                    if b == 2 * a:
                        ans = max(ans, length)

        return ans
