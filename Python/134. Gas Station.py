class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = curr_tank = start = 0

        for idx in range(len(gas)):
            total_tank += gas[idx] - cost[idx]
            curr_tank += gas[idx] - cost[idx]

            if curr_tank < 0:
                start = idx + 1
                curr_tank = 0

        return -1 if total_tank < 0 else start
