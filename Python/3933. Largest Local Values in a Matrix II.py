class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        count = 0
        pairs = {}

        for i in range(n):
            for j in range(m):
                num = matrix[i][j]

                if num > 0:
                    pairs.setdefault(num, []).append([i, j])

        nums = sorted(pairs.keys())

        for num in nums:
            for i, j in pairs[num]:
                ok = True

                for bigger in range(num + 1, nums[-1] + 1):
                    if bigger not in pairs:
                        continue

                    for r, c in pairs[bigger]:
                        dr, dc = abs(r - i), abs(c - j)

                        if dr <= num and dc <= num and (dr != num or dc != num):
                            ok = False
                            break

                    if not ok:
                        break

                count += 1 if ok else 0

        return count
