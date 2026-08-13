class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # # method1 time: O(n), space: O(n)
        # n = len(A)
        # count = {}
        # ans = [0] * n

        # for i in range(n):
        #     a = A[i]
        #     b = B[i]

        #     cnt = ans[i - 1] if i > 0 else 0

        #     count[a] = count.get(a, 0) + 1
        #     cnt += 1 if count[a] == 0 else 0

        #     count[b] = count.get(b, 0) - 1
        #     cnt += 1 if count[b] == 0 else 0

        #     ans[i] = cnt

        # return ans

        # method2
        n = len(A)
        count = {}
        ans = []
        common = 0

        for i in range(n):
            a = A[i]
            b = B[i]

            count[a] = count.get(a, 0) + 1

            if count[a] == 2:
                common += 1

            count[b] = count.get(b, 0) + 1

            if count[b] == 2:
                common += 1

            ans.append(common)

        return ans
