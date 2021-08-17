class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.current_length = 0
        self.stack = []

    def push(self, x: int) -> None:
        if self.current_length+1 <= self.maxSize:
            self.stack.append(x)
            self.current_length += 1

    def pop(self) -> int:
        if self.current_length > 0:
            self.current_length -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        idx = 0
        while idx < k and idx < self.current_length:
            self.stack[idx] += val
            idx += 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
