from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        hash_table = {'++X': 1, 'X++': 1, '--X': -1, 'X--': -1}
        x = 0
        for op in operations:
            x += hash_table[op]
        return x


if __name__ == '__main__':
    #ex1    ans:    1
    operations = ["--X", "X++", "X++"]
    print(Solution().finalValueAfterOperations(operations=operations))

    #ex2    ans:    3
    operations = ["++X", "++X", "X++"]
    print(Solution().finalValueAfterOperations(operations=operations))

    #ex3    ans:    0
    operations = ["X++", "++X", "--X", "X--"]
    print(Solution().finalValueAfterOperations(operations=operations))
