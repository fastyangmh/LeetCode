class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        max_count = 0

        for task in tasks:
            counter[task] = 1 + counter.get(task, 0)
            max_count = max(max_count, counter[task])

        max_count_tasks = sum(1 for c in counter.values() if c == max_count)

        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)
