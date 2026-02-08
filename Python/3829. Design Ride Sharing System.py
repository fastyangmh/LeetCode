from collections import deque


class RideSharingSystem:
    def __init__(self):
        self.riders = deque()
        self.drivers = deque()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.drivers and self.riders:
            return [self.drivers.popleft(), self.riders.popleft()]

        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        stack = []

        while self.riders:
            if self.riders[0] == riderId:
                self.riders.popleft()
                break
            stack.append(self.riders.popleft())

        while stack:
            self.riders.appendleft(stack.pop())


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
