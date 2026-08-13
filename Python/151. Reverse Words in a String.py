class Solution:
    def reverseWords(self, s: str) -> str:
        # # method1 time: O(n), space: O(n)
        # return " ".join(reversed(s.split()))

        # method2 time: O(n), space: O(n)
        n = len(s)
        stack = []
        left = 0

        while left < n and s[left] == " ":
            left += 1

        right = left

        while right < n:
            char = s[right]

            if char == " ":
                stack.append(s[left:right])

                while right < n and s[right] == " ":
                    right += 1

                left = right
            else:
                right += 1

        if left != right:
            stack.append(s[left:right])

        ans = []

        while stack:
            ans.append(stack.pop())

            if stack:
                ans.append(" ")

        return "".join(ans)
