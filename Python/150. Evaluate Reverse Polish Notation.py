from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacks = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stacks.append(int(token))
            else:
                b = stacks.pop()
                a = stacks.pop()
                res = 0

                if token == "+":
                    res = a + b
                elif token == "-":
                    res = a - b
                elif token == "*":
                    res = a * b
                else:
                    res = int(a / b)

                stacks.append(res)

        return stacks[-1]
