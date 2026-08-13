class Solution:
    def decodeString(self, s: str) -> str:
        curr_count = 0
        curr_string = ""
        stack = []

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
                curr_string = prev_string + curr_string * prev_count

        return curr_string
