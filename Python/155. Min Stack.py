class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = None

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.curr_min = value
        else:
            diff = value - self.curr_min
            self.stack.append(diff)
            self.curr_min = value if diff < 0 else self.curr_min

    def pop(self) -> None:
        diff = self.stack.pop()
        self.curr_min = self.curr_min - diff if diff < 0 else self.curr_min

    def top(self) -> int:
        diff = self.stack[-1]
        return self.curr_min + diff if diff > 0 else self.curr_min

    def getMin(self) -> int:
        return self.curr_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
