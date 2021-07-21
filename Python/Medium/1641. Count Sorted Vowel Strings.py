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
