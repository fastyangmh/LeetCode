class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}

        for t in tasks:
            counter[t] = counter.get(t, 0) + 1

        max_count = max(counter.values())
        num_max_count_task = sum(1 for count in counter.values() if count == max_count)

        return max(len(tasks), (max_count - 1) * (n + 1) + num_max_count_task)
