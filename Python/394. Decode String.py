class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        curr_count = 0

        for c in s:
            if c.isdigit():
                curr_count = curr_count * 10 + int(c)
            elif c.isalpha():
                curr_string += c
            elif c == "[":
                stack.append((curr_count, curr_string))

                curr_count = 0
                curr_string = ""
            else:
                prev_count, prev_string = stack.pop()

                curr_string = prev_string + prev_count * curr_string

        return curr_string
