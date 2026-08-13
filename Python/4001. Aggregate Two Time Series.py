class Solution:
    def aggregateTimeSeries(
        self, series1: list[list[int]], series2: list[list[int]]
    ) -> list[list[int]]:
        i = len(series1) - 1
        j = len(series2) - 1

        curr1 = curr2 = 0
        ans = []

        while i >= 0 or j >= 0:
            if j < 0 or (i >= 0 and series1[i][0] > series2[j][0]):
                t = series1[i][0]
            elif i < 0 or series2[j][0] > series1[i][0]:
                t = series2[j][0]
            else:
                t = series1[i][0]

            if i >= 0 and series1[i][0] == t:
                curr1 = series1[i][1]
                i -= 1

            if j >= 0 and series2[j][0] == t:
                curr2 = series2[j][1]
                j -= 1

            ans.append((t, curr1 + curr2))

        ans.reverse()

        return ans
