from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # # method1
        # if endWord not in wordList:
        #     return 0

        # L = len(beginWord)
        # all_combos = defaultdict(list)

        # for word in wordList:
        #     for i in range(L):
        #         pattern = word[:i] + "*" + word[i + 1 :]
        #         all_combos[pattern].append(word)

        # queue = deque([(beginWord, 1)])
        # visited = set([beginWord])

        # while queue:
        #     word, level = queue.popleft()

        #     for i in range(L):
        #         pattern = word[:i] + "*" + word[i + 1 :]

        #         for neighbor in all_combos[pattern]:
        #             if neighbor == endWord:
        #                 return level + 1

        #             if neighbor not in visited:
        #                 visited.add(neighbor)
        #                 queue.append((neighbor, level + 1))

        #         all_combos[pattern].clear()

        # return 0

        # method2
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        begin_set = {beginWord}
        end_set = {endWord}
        word_set = set(wordList)

        level = 1

        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_level = set()

            for word in begin_set:
                for i in range(L):
                    for c in range(ord("a"), ord("z") + 1):
                        new_word = word[:i] + chr(c) + word[i + 1 :]

                        if new_word in end_set:
                            return level + 1

                        if new_word in word_set:
                            word_set.remove(new_word)
                            next_level.add(new_word)

            level += 1
            begin_set = next_level

        return 0
