class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for curr in asteroids:
            while stack and stack[-1] > 0 and curr < 0:
                if stack[-1] < abs(curr):
                    stack.pop()
                elif stack[-1] > abs(curr):
                    curr = None
                    break
                else:
                    stack.pop()
                    curr = None
                    break

            if curr is not None:
                stack.append(curr)

        return stack
