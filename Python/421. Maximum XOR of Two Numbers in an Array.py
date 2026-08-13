class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # # method1
        # class TrieNode:
        #     def __init__(self):
        #         self.child = [None, None]

        # class Trie:
        #     def __init__(self):
        #         self.root = TrieNode()

        #     def insert(self, num):
        #         node = self.root

        #         for i in range(31, -1, -1):
        #             bit = (num >> i) & 1

        #             if node.child[bit] is None:
        #                 node.child[bit] = TrieNode()

        #             node = node.child[bit]

        #     def query(self, num):
        #         node = self.root
        #         ans = 0

        #         for i in range(31, -1, -1):
        #             bit = (num >> i) & 1
        #             opposite = bit ^ 1

        #             if node.child[opposite] is not None:
        #                 ans |= 1 << i
        #                 node = node.child[opposite]
        #             else:
        #                 node = node.child[bit]

        #         return ans

        # trie = Trie()

        # for num in nums:
        #     trie.insert(num)

        # ans = 0

        # for num in nums:
        #     ans = max(ans, trie.query(num))

        # return ans

        # method2
        ans = 0
        mask = 0

        for i in range(31, -1, -1):
            mask |= 1 << i

            prefixes = set()

            for num in nums:
                prefixes.add(num & mask)

            candidate = ans | (1 << i)

            for p in prefixes:
                if (p ^ candidate) in prefixes:
                    ans = candidate
                    break

        return ans
