import bisect


class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        total = 0
        prefix = []

        for task_time in tasks:
            total += task_time
            prefix.append(total)

        ans = []
        progress = 0

        for shift_time in shifts:
            remaining = total - progress

            if shift_time >= remaining:
                ans.append(0)
                progress = 0
            else:
                progress += shift_time
                completed = bisect.bisect_right(prefix, progress)
                ans.append(n - completed)

        return ans
