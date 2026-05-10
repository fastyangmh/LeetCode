from collections import Counter


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set = set("aeiou")
        vowels = [ch for ch in s if ch in vowels_set]

        freq = Counter(vowels)
        first_index = {}

        for i, ch in enumerate(s):
            if ch in vowels_set and ch not in first_index:
                first_index[ch] = i

        vowels.sort(key=lambda x: (-freq[x], first_index[x]))

        res = list(s)
        vowels_idx = 0

        for i in range(len(s)):
            if res[i] in vowels_set:
                res[i] = vowels[vowels_idx]
                vowels_idx += 1

        return "".join(res)
