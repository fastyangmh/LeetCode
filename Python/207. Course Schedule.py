from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # method1
        # graph = {c: [] for c in range(numCourses)}
        # visited = [0] * numCourses

        # for a, b in prerequisites:
        #     graph[b].append(a)

        # def dfs(course):
        #     if visited[course] == 1:
        #         return False

        #     if visited[course] == 2:
        #         return True

        #     visited[course] = 1

        #     for next_course in graph[course]:
        #         if not dfs(next_course):
        #             return False

        #     visited[course] = 2

        #     return True

        # for course in range(numCourses):
        #     if not dfs(course):
        #         return False

        # return True

        # method2
        graph = {c: [] for c in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([c for c in range(numCourses) if indegree[c] == 0])
        finished = 0

        while queue:
            course = queue.popleft()
            finished += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return finished == numCourses
