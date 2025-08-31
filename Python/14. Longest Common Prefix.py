from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # method1
        pref = strs[0]

        for s in strs[1:]:
            while s[: len(pref)] != pref:
                pref = pref[:-1]

                if not pref:
                    return ""

        return pref

        # method2
        # class TrieNode:
        #     def __init__(self):
        #         self.children = {}
        #         self.is_end = False

        # root = TrieNode()

        # for word in strs:
        #     node = root
        #     for c in word:
        #         if c not in node.children:
        #             node.children[c] = TrieNode()
        #         node = node.children[c]
        #     node.is_end = True

        # node = root
        # pref = ""

        # while node and len(node.children) == 1 and not node.is_end:
        #     ch = next(iter(node.children))
        #     pref += ch
        #     node = node.children[ch]

        # return pref
