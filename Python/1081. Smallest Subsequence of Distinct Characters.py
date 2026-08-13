class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_position = {char: idx for idx, char in enumerate(s)}
        stack = []
        in_stack = set()

        for idx, char in enumerate(s):
            if char in in_stack:
                continue

            while stack and stack[-1] > char and last_position[stack[-1]] > idx:
                top = stack.pop()
                in_stack.remove(top)

            stack.append(char)
            in_stack.add(char)

        return "".join(stack)
