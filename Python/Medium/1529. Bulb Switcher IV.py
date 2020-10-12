class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        step = 0
        x = '0'*n
        idx = 0
        while step != n:
            if x == target:
                idx += 1
                break
            elif x[idx] != target[idx]:
                if x[idx] == '0':
                    x = x[:idx]+'1'*len(x[idx:])
                else:
                    x = x[:idx]+'0'*len(x[idx:])
                idx += 1
                step += 1
            else:
                idx += 1
        return step
        # return 2*target.count('10')+(target[-1]==1)


if __name__ == "__main__":
    target = "10111"
    print(Solution().minFlips(target=target))
    target = "00000"
    print(Solution().minFlips(target=target))
    target = "001011101"
    print(Solution().minFlips(target=target))
