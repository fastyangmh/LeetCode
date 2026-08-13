class Logger:
    def __init__(self):
        self.last_seen = {}
        self.limit = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_seen:
            self.last_seen[message] = timestamp
            return True

        if timestamp - self.last_seen[message] >= self.limit:
            self.last_seen[message] = timestamp
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
