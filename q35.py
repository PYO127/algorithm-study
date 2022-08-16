# p346 Q35. 조합
from typing import List
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            for e in range(start, n + 1):
                elements.append(e)
                dfs(elements, e + 1, k - 1)
                elements.pop()

        dfs([], 1, k)

        return results

    def combine_itertools(self, n:int, k:int) -> List[List[int]]:
        return list(map(list,itertools.combinations(range(1,n+1),k)))