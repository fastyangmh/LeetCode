class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # # method1
        # MOD = 10**9 + 7

        # n = len(arr)
        # left = [0] * n
        # right = [0] * n

        # stack = []

        # for i in range(n):
        #     while stack and arr[stack[-1]] > arr[i]:
        #         stack.pop()

        #     if stack:
        #         left[i] = i - stack[-1]
        #     else:
        #         left[i] = i + 1

        #     stack.append(i)

        # stack = []

        # for i in range(n - 1, -1, -1):
        #     while stack and arr[stack[-1]] >= arr[i]:
        #         stack.pop()

        #     if stack:
        #         right[i] = stack[-1] - i
        #     else:
        #         right[i] = n - i

        #     stack.append(i)

        # ans = 0

        # for i in range(n):
        #     ans += arr[i] * left[i] * right[i]

        # return ans % MOD

        # method2
        MOD = 10**9 + 7

        arr = [0] + arr + [0]
        ans = 0
        stack = []

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                curr = stack.pop()

                ans += arr[curr] * (curr - stack[-1]) * (i - curr)

            stack.append(i)

        return ans % MOD
