from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = []
        queue = []+[start]
        while len(queue) > 0:
            step = arr[start]
            feed_idx = start+step if (start+step) < n else None
            back_idx = start-step if (start-step) >= 0 else None
            if feed_idx is not None:
                if arr[feed_idx] == 0:
                    return True
                else:
                    queue.append(feed_idx)
            if back_idx is not None:
                if arr[back_idx] == 0:
                    return True
                else:
                    queue.append(back_idx)
            seen.append(start)
            start = queue.pop()
            while start in seen:
                if len(queue):
                    start = queue.pop()
                else:
                    break
        return False


if __name__ == "__main__":
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    print(Solution().canReach(arr=arr, start=start))
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 0
    print(Solution().canReach(arr=arr, start=start))
    arr = [3, 0, 2, 1, 2]
    start = 2
    print(Solution().canReach(arr=arr, start=start))
    arr = [0, 1]
    start = 1
    print(Solution().canReach(arr=arr, start=start))
    arr = [1, 1, 1, 1, 1, 1, 1, 1, 0]
    start = 3
    print(Solution().canReach(arr=arr, start=start))
    arr = [4, 4, 1, 3, 0, 3]
    start = 2
    print(Solution().canReach(arr=arr, start=start))
