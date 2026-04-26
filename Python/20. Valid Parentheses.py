class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in {"(", "{", "["}:
                stack.append(c)
            else:
                t = stack.pop() if stack else ""

                if t + c not in {"()", "{}", "[]"}:
                    return False

        return not stack
