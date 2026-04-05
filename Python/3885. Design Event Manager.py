import heapq


class EventManager:
    def __init__(self, events: list[list[int]]):
        self.priorities = {}
        self.heap = []

        for eid, p in events:
            self.priorities[eid] = p
            heapq.heappush(self.heap, (-p, eid))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.priorities[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            neg_p, eid = heapq.heappop(self.heap)

            if eid in self.priorities and self.priorities[eid] == -neg_p:
                self.priorities.pop(eid)
                return eid

        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
