class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in "({[":
                stack.append(p)
            else:
                if not stack:
                    return False
                if stack.pop() + p not in {"()", "{}", "[]"}:
                    return False

        return not stack
