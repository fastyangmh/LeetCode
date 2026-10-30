class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for c in operations:
            if c.isdigit() or c[0] == "-":
                stack.append(int(c))
            elif c == "+":
                stack.append(stack[-1] + stack[-2])
            elif c == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.pop()

        return sum(stack)
