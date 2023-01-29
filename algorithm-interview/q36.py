# p351 Q36. 조합의 합
from typing import List


class solution:
    def CombinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path[:])
                # result.append(path) <- 책에는 이것처럼 되어있는데, 깊은 복사사용 X
                return
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


