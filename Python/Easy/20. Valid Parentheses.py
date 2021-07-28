class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for v in s:
            if len(stack):
                if stack[-1]+v in ['()', '[]', '{}']:
                    stack.pop()
                    continue
            stack.append(v)
        if len(stack):
            return False
        else:
            return True


if __name__ == '__main__':
    # ex1    ans true
    s = "()"
    print(Solution().isValid(s=s))

    # ex2    ans true
    s = "()[]{}"
    print(Solution().isValid(s=s))

    # ex3    ans false
    s = "(]"
    print(Solution().isValid(s=s))

    # ex4    ans false
    s = "([)]"
    print(Solution().isValid(s=s))

    # ex5    ans true
    s = "{[]}"
    print(Solution().isValid(s=s))
