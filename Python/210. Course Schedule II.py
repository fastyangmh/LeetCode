from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # method1
        graph = {c: [] for c in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([course for course, ind in enumerate(indegree) if ind == 0])
        finished = 0
        ordering = []

        while queue:
            course = queue.popleft()
            ordering.append(course)
            finished += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return ordering if finished == numCourses else []

        # # method2 #NOTE: dfs is post-order traversal, left -> right -> root
        # graph = {c: [] for c in range(numCourses)}
        # visited = [0] * numCourses
        # ordering = []

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
        #     ordering.append(course)

        #     return True

        # finished = 0

        # for course in range(numCourses):
        #     if not dfs(course):
        #         continue

        #     finished += 1

        # return ordering[::-1] if finished == numCourses else []
