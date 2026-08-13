class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev_end = 0

        for start, end in intervals:
            if start < prev_end:
                return False
            prev_end = end

        return True
