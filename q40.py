# p373 Q40. 네트워크 딜레이 타임
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        Q = [(0, k)]
        # heappush(), heappop() 연산을 이용하기 위해
        # 거리값을 첫 번째 원소로 사용한다.
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        dist = defaultdict(int)

        # 다익스트라 알고리즘
        while Q:
            # heappop() -> 첫 번째 값 기준으로 최소힙 구성 (여기서는 cost)
            # 한 노드 x에 대해 여러 값의 거리가 Q에 존재할 수 있으나,
            # heappop(), heappush() 연산을 사용하므로,
            # 항상 최소거리의 (거리, 노드 x)가 최초로 pop 되고,
            # 그 값으로 dist를 update 한다.
            # 거리가 큰 값은 나중에 pop() 되긴하지만, not in 연산에 의해,
            # 이미 dist에 값이 존재하므로 무시된다.
            cost, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = cost
                for v, w in graph[node]:
                    alt = w + cost
                    heapq.heappush(Q, (alt, v))

        if len(dist) != n:
            return -1
        return max(dist.values())


