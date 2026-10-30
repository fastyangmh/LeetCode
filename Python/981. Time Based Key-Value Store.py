class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, []).append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.data.get(key, [])

        l, r = 0, len(values) - 1
        ret = ""

        while l <= r:
            m = (l + r) // 2

            if values[m][0] <= timestamp:
                ret = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return ret


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
