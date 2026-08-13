class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # # method1
        # class TrieNode:
        #     def __init__(self):
        #         self.children = {}

        # root = TrieNode()

        # for num in arr1:
        #     node = root

        #     for c in str(num):
        #         if c not in node.children:
        #             node.children[c] = TrieNode()
        #         node = node.children[c]

        # ans = 0

        # for num in arr2:
        #     node = root
        #     prefix = 0

        #     for c in str(num):
        #         if c not in node.children:
        #             break
        #         prefix += 1
        #         node = node.children[c]

        #     ans = max(ans, prefix)

        # return ans

        # method2
        prefixes = set()

        for num in arr1:
            while num:
                if num in prefixes:
                    break
                prefixes.add(num)
                num //= 10

        maximum_prefix = 0

        for num in arr2:
            while num > maximum_prefix:
                if num in prefixes:
                    maximum_prefix = num
                    break
                num //= 10

        return len(str(maximum_prefix)) if maximum_prefix else 0
