class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
                continue

            a, b = stack.pop(), stack.pop()

            if t == "+":
                stack.append(b + a)
            elif t == "-":
                stack.append(b - a)
            elif t == "*":
                stack.append(b * a)
            else:
                stack.append(int(b / a))

        return stack.pop()
