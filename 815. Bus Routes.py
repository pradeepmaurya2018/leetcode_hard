import collections
from typing import List


class Solution:
    visited = {}
    steps = 0
    answerFound = False
    routesMaap = collections.defaultdict(list)

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = collections.defaultdict(list)
        for i, ro in enumerate(routes):
            j = 0
            while j < len(ro) - 1:
                s = ro[j]
                d = ro[j + 1]
                graph[s].append(d)
                j += 1
                if i not in self.routesMaap[s]:
                    self.routesMaap[s].append(i)
                if i not in self.routesMaap[d]:
                    self.routesMaap[d].append(i)
            graph[ro[len(ro) - 1]].append(ro[0])
        self.visited[source] = 1
        self.steps = 1
        self.answerFound = False
        self.numBusesToDestinationUtil(graph, source, target)
        # print(graph)
        # print(routesMaap)
        if self.answerFound:
            return self.steps
        else:
            return -1

    def numBusesToDestinationUtil(self, graph, source: int, target: int):
        if source == target:
            print("Found the target", self.steps)
            self.answerFound = True
            return
        for v in graph[source]:
            if self.visited.get(v) != 1:
                if len(self.routesMaap[source]) == len(self.routesMaap[v]) and self.routesMaap[source][0] != \
                        self.routesMaap[v][0]:
                    self.steps += 1
                self.visited[v] = 1
                self.numBusesToDestinationUtil(graph, v, target)


print(Solution().numBusesToDestination([[2], [2, 8]]
                                       , source=8, target=2))
