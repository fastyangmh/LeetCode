class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = fast = i

            while True:
                if (nums[slow] > 0) != direction:
                    break

                next_fast = next_index(fast)

                if (nums[fast] > 0) != direction or (nums[next_fast] > 0) != direction:
                    break

                slow = next_index(slow)
                fast = next_index(next_index(fast))

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            curr = i

            while nums[curr] != 0 and (nums[curr] > 0) == direction:
                nxt = next_index(curr)
                nums[curr] = 0
                curr = nxt

        return False
