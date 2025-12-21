class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if b in {"(", "{", "["}:
                stack.append(b)
            else:
                t = stack.pop() if stack else ""

                if t + b not in {"()", "{}", "[]"}:
                    return False

        return not stack
