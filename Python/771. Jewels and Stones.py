class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for j in J:
            count += list(S).count(j)
        return count


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(Solution().numJewelsInStones(J, S))
    J = "z"
    S = "ZZ"
    print(Solution().numJewelsInStones(J, S))
