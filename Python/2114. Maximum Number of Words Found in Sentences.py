from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most_length = 0
        for sentence in sentences:
            l = 0
            for char in sentence:
                if char == ' ':
                    l += 1
            if l > most_length:
                most_length = l
        return most_length + 1
        '''
        fatest solution
        ans = 0
        for s in sentences:
            ans = max(ans, len(s.split()))
        return ans
        '''


if __name__ == '__main__':
    #ex1    ans:    6
    sentences = [
        "alice and bob love leetcode", "i think so too",
        "this is great thanks very much"
    ]
    print(Solution().mostWordsFound(sentences=sentences))

    #ex2    ans:    3
    sentences = ["please wait", "continue to fight", "continue to win"]
    print(Solution().mostWordsFound(sentences=sentences))
