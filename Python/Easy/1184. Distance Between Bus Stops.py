from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        a = sum(distance[start:destination])
        b = sum(distance)-a
        return min(a, b)
        '''
        n = len(distance)
        feed_dis = 0
        back_dis = 0
        if start > destination:
            start, destination = destination, start
        for idx in range(start, destination):
            feed_dis += distance[idx]
        step = n-(destination-start)
        for idx in range(1, step):
            temp = (destination+idx) % n
            back_dis += distance[temp]
        return min(feed_dis, back_dis)
        '''


if __name__ == "__main__":
    distance = [1, 2, 3, 4]
    start = 0
    destination = 1
    print(Solution().distanceBetweenBusStops(
        distance=distance, start=start, destination=destination))
    distance = [1, 2, 3, 4]
    start = 0
    destination = 2
    print(Solution().distanceBetweenBusStops(
        distance=distance, start=start, destination=destination))
    distance = [1, 2, 3, 4]
    start = 0
    destination = 3
    print(Solution().distanceBetweenBusStops(
        distance=distance, start=start, destination=destination))
    distance = [7, 10, 1, 12, 11, 14, 5, 0]
    start = 7
    destination = 2
    print(Solution().distanceBetweenBusStops(
        distance=distance, start=start, destination=destination))
