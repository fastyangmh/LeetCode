class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        n = len(nums)

        next_smaller = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                next_smaller[i] = stack[-1]

            stack.append(i)

        bit = [0] * (n + 1)

        def add(index):
            index += 1

            while index <= n:
                bit[index] += 1
                index += index & -index

        def prefix_sum(index):
            if index < 0:
                return 0

            index += 1
            total = 0

            while index > 0:
                total += bit[index]
                index -= index & -index

            return total

        def range_sum(left, right):
            if left > right:
                return 0

            return prefix_sum(right) - prefix_sum(left - 1)

        order = sorted(range(n), key=lambda i: nums[i], reverse=True)

        ans = 0
        p = 0

        while p < n:
            q = p
            value = nums[order[q]]

            while q < n and nums[order[q]] == value:
                q += 1

            for t in range(p, q):
                i = order[t]

                left = i + 1
                right = next_smaller[i] - 1

                ans += range_sum(left, right)

            for t in range(p, q):
                add(order[t])

            p = q

        return ans
