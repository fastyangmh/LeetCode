class WordDictionary:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end

            char = word[idx]

            if char == ".":
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True

                return False
            elif char in node.children:
                return dfs(node.children[char], idx + 1)
            else:
                return False

        return dfs(self, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
