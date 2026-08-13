class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in {"(", "[", "{"}:
                stack.append(p)
            else:
                if not stack or stack[-1] + p not in {"()", "[]", "{}"}:
                    return False
                stack.pop()

        return len(stack) == 0
