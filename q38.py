# p357 Q38. 일정 재구성
from collections import defaultdict, deque
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. 우선 정렬부터해주고, dict에 추가해주자 (2번째 목록 기준 정렬)
        tickets.sort()  # 굳이 key 안 써줘도 된다.
        graph = defaultdict(list)
        for a, b in tickets:
            graph[a].append(b)

        path = []

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]


    def findItinerary_2(self, tickets: List[List[str]]) -> List[str]:
        # 1. 우선 정렬부터해주고, dict에 추가해주자 (2번째 목록 기준 정렬)
        tickets.sort()  # 굳이 key 안 써줘도 된다.
        graph = defaultdict(list)
        for a, b in tickets:
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')

        return route[::-1]