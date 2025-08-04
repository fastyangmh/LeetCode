from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        lead = 0
        hashTable = []
        result = {}.fromkeys(persons, 0)
        for p in persons:
            result[p] += 1
            if result[lead] <= result[p]:
                lead = p
            hashTable.append(lead)
        self.hashTable = hashTable

    def q(self, t: int) -> int:
        idx = self.binary_search(self.times, t)-1
        return self.hashTable[idx]

    def binary_search(self, sequence, target):
        low = 0
        high = len(sequence) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            # Check if target is present at mid
            if sequence[mid] < target:
                low = mid + 1
            # If target is greater, ignore left half
            elif sequence[mid] > target:
                high = mid - 1
            # If target is smaller, ignore right half
            else:
                return mid+1
        return high+1


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

if __name__ == "__main__":
    # example
    action = ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    t = [3, 12, 25, 15, 24, 8]
    output = []
    for idx, s in enumerate(action):
        if s == 'TopVotedCandidate':
            obj = TopVotedCandidate(persons=persons, times=times)
            output.append('null')
        elif s == 'q':
            output.append(obj.q(t=t[idx-1]))
    print(output)

    # 12/97
    action = ["TopVotedCandidate", "q", "q",
              "q", "q", "q", "q", "q", "q", "q", "q"]
    persons = [0, 1, 2, 2, 1]
    times = [20, 28, 29, 54, 56]
    t = [28, 53, 57, 29, 29, 28, 30, 20, 56, 55]
    output = []
    for idx, s in enumerate(action):
        if s == 'TopVotedCandidate':
            obj = TopVotedCandidate(persons=persons, times=times)
            output.append('null')
        elif s == 'q':
            output.append(obj.q(t=t[idx-1]))
    print(output)

    # 14/97
    action = ["TopVotedCandidate", "q", "q",
              "q", "q", "q", "q", "q", "q", "q", "q"]
    persons = [0, 0, 1, 1, 2]
    times = [0, 67, 69, 74, 87]
    t = [4, 62, 100, 88, 70, 73, 22, 75, 29, 10]
    output = []
    for idx, s in enumerate(action):
        if s == 'TopVotedCandidate':
            obj = TopVotedCandidate(persons=persons, times=times)
            output.append('null')
        elif s == 'q':
            output.append(obj.q(t=t[idx-1]))
    print(output)

    # 15/97
    action = ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    t = [3, 12, 25, 15, 24, 8]
    output = []
    for idx, s in enumerate(action):
        if s == 'TopVotedCandidate':
            obj = TopVotedCandidate(persons=persons, times=times)
            output.append('null')
        elif s == 'q':
            output.append(obj.q(t=t[idx-1]))
    print(output)

    # 16/97
    action = ["TopVotedCandidate", "q", "q",
              "q", "q", "q", "q", "q", "q", "q", "q"]
    persions = [0, 0, 1, 1, 2]
    times = [0, 67, 69, 74, 87]
    t = [4, 62, 100, 88, 70, 73, 22, 75, 29, 10]
    output = []
    for idx, s in enumerate(action):
        if s == 'TopVotedCandidate':
            obj = TopVotedCandidate(persons=persons, times=times)
            output.append('null')
        elif s == 'q':
            output.append(obj.q(t=t[idx-1]))
    print(output)

    # 62/97
    action = ["TopVotedCandidate", "q", "q",
              "q", "q", "q", "q", "q", "q", "q", "q"]
    persons = [0, 1, 2, 2, 1]
    times = [20, 28, 29, 54, 56]
    t = [28, 53, 57, 29, 29, 28, 30, 20, 56, 55]
    output = []
    for idx, s in enumerate(action):
        if s == 'TopVotedCandidate':
            obj = TopVotedCandidate(persons=persons, times=times)
            output.append('null')
        elif s == 'q':
            output.append(obj.q(t=t[idx-1]))
    print(output)
