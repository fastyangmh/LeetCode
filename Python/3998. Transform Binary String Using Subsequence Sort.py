class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        n = len(s)

        prefix = [0] * n
        total_ones = 0

        for i, c in enumerate(s):
            total_ones += 1 if c == "1" else 0
            prefix[i] = total_ones

        ans = []

        for t in strs:
            fixed_ones = t.count("1")
            question_marks = t.count("?")

            need = total_ones - fixed_ones

            if need < 0 or need > question_marks:
                ans.append(False)
                continue

            suffix_q = [0] * (n + 1)

            for i in range(n - 1, -1, -1):
                suffix_q[i] += suffix_q[i + 1] + (1 if t[i] == "?" else 0)

            curr_ones = 0
            possible = True

            for i, c in enumerate(t):
                if c == "1":
                    curr_ones += 1
                elif c == "?":
                    if need > suffix_q[i + 1]:
                        need -= 1
                        curr_ones += 1

                if curr_ones > prefix[i]:
                    possible = False
                    break

            ans.append(possible)

        return ans
