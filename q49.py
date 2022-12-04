# p416 Q49. 최소 높이 트리
from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        for v0, v1 in edges:
            graph[v0].append(v1)
            graph[v1].append(v0)  # undirected graph

        leaves = []
        for v0 in graph:
            if len(graph[v0]) == 1:
                leaves.append(v0)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop() # 어차피 원소가 1개 밖에 없으니까
                graph.pop(leaf) # 나뭇잎 제거
                graph[neighbor].remove(leaf) # 나뭇잎에 연결된 이웃에서 나뭇잎 가지 제거

            # for v0 in graph:
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
