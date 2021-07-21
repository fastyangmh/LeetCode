class Solution:
    def countVowelStrings(self, n: int) -> int:
        array = [1]*5  # a, e, i, o, u
        last_sum = sum(array)
        for _ in range(1, n):
            temp = []
            for j in range(5):
                if j == 0:
                    temp.append(last_sum)
                else:
                    temp.append(temp[j-1]-array[j-1])
            array = temp
            last_sum = sum(array)
        return last_sum

    ''' other solution, this is funny
    class Solution:
    def countVowelStrings(self, n: int) -> int:
        # a, e, i, o, u
        transformation_matrix = [[1, 1, 1, 1, 1],
                                 [0, 1, 1, 1, 1],
                                 [0, 0, 1, 1, 1],
                                 [0, 0, 0, 1, 1],
                                 [0, 0, 0, 0, 1]]
        v_counts = [1]*5
        for _ in range(n-1):
            v_counts = [self.dot(v_counts, row)
                        for row in transformation_matrix]
        return sum(v_counts)

    def dot(self, l1, l2):
        return sum([x*y for x, y in zip(l1, l2) if y != 0])
    '''


if __name__ == '__main__':
    # ex1    ans 5
    n = 1
    print(Solution().countVowelStrings(n=n))

    # ex2    ans 15
    n = 2
    print(Solution().countVowelStrings(n=n))

    # ex3    ans 66045
    n = 33
    print(Solution().countVowelStrings(n=n))
