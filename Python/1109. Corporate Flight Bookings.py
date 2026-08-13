class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # # method1 time: O(m+n), space: O(n)
        # diff = [0] * (n + 2)

        # for first, last, seats in bookings:
        #     diff[first] += seats
        #     diff[last + 1] -= seats

        # for idx in range(1, n + 1):
        #     diff[idx] += diff[idx - 1]

        # return diff[1:-1]

        # method2 time: O(m+n), space: O(n)
        diff = [0] * n

        for first, last, seats in bookings:
            diff[first - 1] += seats

            if last < n:
                diff[last] -= seats

        for idx in range(1, n):
            diff[idx] += diff[idx - 1]

        return diff
