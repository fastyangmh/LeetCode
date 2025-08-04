class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ''
        for v in s:
            temp += str(ord(v)-96)
        for idx in range(k):
            ans = 0
            for v in temp:
                ans += int(v)
            temp = str(ans)
        return ans


if __name__ == '__main__':
    # ex1    ans    36
    s = "iiii"
    k = 1
    print(Solution().getLucky(s=s, k=k))
    # ex2    ans    6
    s = "leetcode"
    k = 2
    print(Solution().getLucky(s=s, k=k))
    # ex3    ans    8
    s = "zbax"
    k = 2
    print(Solution().getLucky(s=s, k=k))
