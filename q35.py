# p346 Q35. 조합
from typing import List
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        elements = []

        def dfs(start, index):
            if index == 0:
                ans.append(elements[:])

            for i in range(start, n + 1):
                elements.append(i)
                dfs(i + 1, index - 1)
                elements.pop()

        dfs(1, k)
        return ans

    def combine_itertools(self, n: int, k: int) -> List[List[int]]:
        # List[Tuple[int]] -> List[List[int]] 변환
        return list(map(list, itertools.combinations(range(1, n + 1), k)))
