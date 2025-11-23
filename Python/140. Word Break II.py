class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == n:
                return [""]

            if start in memo:
                return memo[start]

            res = []

            for end in range(start + 1, n + 1):
                word = s[start:end]

                if word not in word_set:
                    continue

                for sub in dfs(end):
                    if sub == "":
                        res.append(word)
                    else:
                        res.append(word + " " + sub)

            memo[start] = res

            return res

        return dfs(0)
