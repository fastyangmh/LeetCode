from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # # method1
        # graph = {}
        # indegree = [0] * numCourses

        # for a, b in prerequisites:
        #     graph.setdefault(b, []).append(a)
        #     indegree[a] += 1

        # queue = deque([k for k, v in enumerate(indegree) if v == 0])
        # ans = []

        # while queue:
        #     node = queue.popleft()
        #     ans.append(node)

        #     for next_course in graph.get(node, []):
        #         indegree[next_course] -= 1

        #         if indegree[next_course] == 0:
        #             queue.append(next_course)

        # return ans if len(ans) == numCourses else []

        # method2
        graph = {}

        for a, b in prerequisites:
            graph.setdefault(b, []).append(a)

        visited = [0] * numCourses
        ans = []

        def dfs(course):
            if visited[course] == 1:
                return False

            if visited[course] == 2:
                return True

            visited[course] = 1

            for next_course in graph.get(course, []):
                if not dfs(next_course):
                    return False

            visited[course] = 2

            ans.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                continue

        return ans[::-1] if len(ans) == numCourses else []
