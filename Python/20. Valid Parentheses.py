# import

# class
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "]": "[", "}": "{"}
        stacks = []

        for c in s:
            if c in mapping:
                top_c = stacks.pop() if stacks else None
                if top_c != mapping[c]:
                    return False
            else:
                stacks.append(c)

        return not stacks


if __name__ == "__main__":
    # Example 1:
    s = "()"
    assert Solution().isValid(s) is True, Solution().isValid(s)

    # Example 2:
    s = "()[]{}"
    assert Solution().isValid(s) is True, Solution().isValid(s)

    # Example 3:
    s = "(]"
    assert Solution().isValid(s) is False, Solution().isValid(s)

    # Example 4:
    s = "([])"
    assert Solution().isValid(s) is True, Solution().isValid(s)

    # 7/100
    s = "]"
    assert Solution().isValid(s) is False, Solution().isValid(s)

    # 9/100
    s = "){"
    assert Solution().isValid(s) is False, Solution().isValid(s)
