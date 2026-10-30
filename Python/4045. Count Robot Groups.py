class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(position)
        stack = []

        for i in range(n - 1, -1, -1):
            merge_time = None

            while stack:
                j, j_merge_time = stack[-1]
                gap = position[j] - position[i]

                if gap <= distance:
                    t_num = 0
                    t_den = 1
                elif speed[i] > speed[j]:
                    t_num = gap - distance
                    t_den = speed[i] - speed[j]
                else:
                    if j_merge_time is not None:
                        stack.pop()
                        continue
                    break

                if j_merge_time is None:
                    merge_time = (t_num, t_den)
                    break

                j_num, j_den = j_merge_time

                if t_num * j_den <= j_num * t_den:
                    merge_time = (t_num, t_den)
                    break

                stack.pop()

            stack.append((i, merge_time))

        return sum(merge_time is None for _, merge_time in stack)
