# method1
class MinStack:
    def __init__(self):
        self._stack = []
        self._min = float("inf")

    def push(self, val: int) -> None:
        self._min = val if self._min > val else self._min
        self._stack.append((val, self._min))

    def pop(self) -> None:
        if self._stack:
            self._stack.pop()
            self._min = float("inf") if not self._stack else self._stack[-1][-1]

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._min


# # method2
# class MinStack:
#     def __init__(self):
#         self._stack = []
#         self._min = None

#     def push(self, val: int) -> None:
#         if not self._stack:
#             self._stack.append(0)
#             self._min = val
#         else:
#             diff = val - self._min
#             self._stack.append(diff)
#             self._min = val if diff < 0 else self._min

#     def pop(self) -> None:
#         if self._stack:
#             diff = self._stack.pop()
#             self._min = self._min - diff if diff < 0 else self._min

#     def top(self) -> int:
#         diff = self._stack[-1]
#         return self._min if diff < 0 else self._min + diff

#     def getMin(self) -> int:
#         return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
