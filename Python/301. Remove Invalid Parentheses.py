from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # # method1
        # left_rem = right_rem = 0
        # res = set()

        # for ch in s:
        #     if ch == "(":
        #         left_rem += 1
        #     elif ch == ")":
        #         if left_rem > 0:
        #             left_rem -= 1
        #         else:
        #             right_rem += 1

        # def dfs(index, left_count, right_count, left_rem, right_rem, path):
        #     if index == len(s):
        #         if left_rem == 0 and right_rem == 0 and left_count == right_count:
        #             res.add("".join(path))
        #         return

        #     ch = s[index]

        #     if ch == "(":
        #         if left_rem > 0:
        #             dfs(
        #                 index + 1,
        #                 left_count,
        #                 right_count,
        #                 left_rem - 1,
        #                 right_rem,
        #                 path,
        #             )

        #         path.append(ch)
        #         dfs(index + 1, left_count + 1, right_count, left_rem, right_rem, path)
        #         path.pop()

        #     elif ch == ")":
        #         if right_rem > 0:
        #             dfs(
        #                 index + 1,
        #                 left_count,
        #                 right_count,
        #                 left_rem,
        #                 right_rem - 1,
        #                 path,
        #             )

        #         if left_count > right_count:
        #             path.append(ch)
        #             dfs(
        #                 index + 1,
        #                 left_count,
        #                 right_count + 1,
        #                 left_rem,
        #                 right_rem,
        #                 path,
        #             )
        #             path.pop()

        #     else:
        #         path.append(ch)
        #         dfs(index + 1, left_count, right_count, left_rem, right_rem, path)
        #         path.pop()

        # dfs(0, 0, 0, left_rem, right_rem, [])

        # return list(res)

        # method2
        def is_valid(substring):
            balanced = 0

            for ch in substring:
                if ch == "(":
                    balanced += 1
                elif ch == ")":
                    balanced -= 1

                    if balanced < 0:
                        return False

            return balanced == 0

        res = []
        found = False
        queue = deque([s])
        visited = {s}

        while queue:
            curr = queue.popleft()

            if is_valid(curr):
                res.append(curr)
                found = True

            if found:
                continue

            for idx in range(len(curr)):
                if curr[idx] not in {"(", ")"}:
                    continue

                new = curr[:idx] + curr[idx + 1 :]

                if new in visited:
                    continue

                queue.append(new)
                visited.add(new)

        return res
