class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        div_indices = {}

        for i, x in enumerate(nums):
            d = 1

            while d * d <= x:
                if x % d == 0:
                    if d > 1:
                        div_indices.setdefault(d, []).append(i)

                    other = x // d

                    if other != d and other > 1:
                        div_indices.setdefault(other, []).append(i)

                d += 1

        if not div_indices:
            return (-min(nums) * 2) % MOD

        prefix = [0]

        for x in nums:
            prefix.append(prefix[-1] + x)

        best_diff = float("-inf")
        best_k = None

        for k, indices in div_indices.items():
            curr = 0
            prev = -1
            local_best = float("-inf")

            for idx in indices:
                if prev == -1:
                    curr = nums[idx]
                else:
                    gap_sum = prefix[idx] - prefix[prev + 1]

                    curr = max(nums[idx], curr - gap_sum + nums[idx])

                local_best = max(local_best, curr)
                prev = idx

            if local_best > best_diff or (local_best == best_diff and k < best_k):
                best_diff = local_best
                best_k = k

        return (best_diff * best_k) % MOD
