class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for v in s:
            if len(stack):
                if v == stack[-1]:
                    stack.pop()
                    continue
            stack.append(v)
        return ''.join(stack)


if __name__ == '__main__':
    # ex1    ans "ca"
    s = "abbaca"
    print(Solution().removeDuplicates(s=s))

    # ex2    ans "ay"
    s = "azxxzy"
    print(Solution().removeDuplicates(s=s))
