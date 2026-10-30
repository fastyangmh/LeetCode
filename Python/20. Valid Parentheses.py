class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in {"(", "{", "["}:
                stack.append(c)
            else:
                if not stack or stack[-1] + c not in {"()", "[]", "{}"}:
                    return False
                stack.pop()

        return not stack
