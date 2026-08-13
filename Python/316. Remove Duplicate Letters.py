class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_position = {char: idx for idx, char in enumerate(s)}

        stack = []
        in_stack = set()

        for idx, char in enumerate(s):
            if char in in_stack:
                continue

            while stack and stack[-1] > char and last_position[stack[-1]] > idx:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(char)
            in_stack.add(char)

        return "".join(stack)
