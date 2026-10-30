from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # # method1
        # words = set(wordList)

        # if endWord not in words:
        #     return 0

        # L = len(beginWord)
        # combs = defaultdict(list)

        # for w in words:
        #     for i in range(L):
        #         pattern = w[:i] + "*" + w[i + 1 :]
        #         combs[pattern].append(w)

        # queue = deque([beginWord])
        # visited = {beginWord}
        # steps = 0

        # while queue:
        #     steps += 1

        #     for _ in range(len(queue)):
        #         w = queue.popleft()

        #         if w == endWord:
        #             return steps

        #         for i in range(L):
        #             pattern = w[:i] + "*" + w[i + 1 :]

        #             for next_word in combs[pattern]:
        #                 if next_word in visited:
        #                     continue

        #                 visited.add(next_word)
        #                 queue.append(next_word)

        # return 0

        # method2
        words = set(wordList)

        if endWord not in words:
            return 0

        L = len(beginWord)

        begin_set = {beginWord}
        end_set = {endWord}

        words.discard(beginWord)
        words.discard(endWord)

        steps = 1

        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_level = set()

            for word in begin_set:
                for i in range(L):
                    prefix = word[:i]
                    suffix = word[i + 1 :]

                    for j in range(26):
                        ch = chr(ord("a") + j)

                        next_word = prefix + ch + suffix

                        if next_word in end_set:
                            return steps + 1

                        if next_word in words:
                            words.remove(next_word)
                            next_level.add(next_word)

            steps += 1
            begin_set = next_level

        return 0
