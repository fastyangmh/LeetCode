# # method1
# class MinStack:
#     def __init__(self):
#         self._stack = []
#         self._min = float("inf")

#     def push(self, val: int) -> None:
#         self._min = val if self._min > val else self._min
#         self._stack.append((val, self._min))

#     def pop(self) -> None:
#         if self._stack:
#             self._stack.pop()
#             self._min = float("inf") if not self._stack else self._stack[-1][-1]

#     def top(self) -> int:
#         return self._stack[-1][0]

#     def getMin(self) -> int:
#         return self._min


# method2
class MinStack:
    def __init__(self):
        self.stack = []
        self.curr_min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.curr_min = val
        else:
            diff = val - self.curr_min
            self.stack.append(diff)
            self.curr_min = val if diff < 0 else self.curr_min

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            self.curr_min = self.curr_min - diff if diff < 0 else self.curr_min

    def top(self) -> int:
        diff = self.stack[-1]
        return self.curr_min if diff < 0 else self.curr_min + diff

    def getMin(self) -> int:
        return self.curr_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
