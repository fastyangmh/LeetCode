from collections import deque


class WordDictionary:

    def __init__(self):
        self.data = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self

        for ch in word:
            if ch not in node.data:
                node.data[ch] = WordDictionary()
            node = node.data[ch]

        node.is_end = True

    def search(self, word: str) -> bool:
        # method1
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end

            ch = word[idx]

            if ch == ".":
                for child in node.data.values():
                    if dfs(child, idx + 1):
                        return True
                return False
            elif ch in node.data:
                return dfs(node.data[ch], idx + 1)
            else:
                return False

        return dfs(self, 0)

        # # method2
        # queue = deque([self])
        # depth = 0

        # while queue and depth < len(word):
        #     ch = word[depth]

        #     for _ in range(len(queue)):
        #         node = queue.popleft()

        #         if ch == ".":
        #             queue.extend([child for child in node.data.values()])

        #         if ch in node.data:
        #             queue.append(node.data[ch])

        #     if not queue:
        #         return False

        #     depth += 1

        # return any(node.is_end for node in queue)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
