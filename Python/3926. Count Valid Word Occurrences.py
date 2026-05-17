class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = "".join(chunks)
        n = len(s)
        i = 0
        freq = {}

        while i < n:
            if s[i].islower():
                j = i

                while j < n:
                    c = s[j]

                    if c.islower():
                        j += 1
                    elif (
                        c == "-"
                        and j > 0
                        and j + 1 < n
                        and s[j - 1].islower()
                        and s[j + 1].islower()
                    ):
                        j += 1
                    else:
                        break

                word = s[i:j]
                freq[word] = freq.get(word, 0) + 1
                i = j

            else:
                i += 1

        return [freq.get(q, 0) for q in queries]
