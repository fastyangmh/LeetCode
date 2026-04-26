class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        max_freq = max(freq.values())
        num_max_freq = sum(1 for v in freq.values() if v == max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max_freq)
