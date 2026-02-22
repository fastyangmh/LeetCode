class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        freq_count = {}

        for freq in num_freq.values():
            freq_count[freq] = freq_count.get(freq, 0) + 1

        for num in nums:
            if freq_count[num_freq[num]] == 1:
                return num

        return -1
