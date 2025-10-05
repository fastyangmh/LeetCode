class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = "+"
        num = 0

        s = s.replace(" ", "")

        for idx, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            if not c.isdigit() or idx == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                num = 0
                sign = c

        return sum(stack)
