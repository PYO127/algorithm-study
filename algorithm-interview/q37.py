# p355 Q37. 부분집합
from typing import List


class solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(path, start):
            results.append(path)
            for i in range(start, len(nums)):
                dfs(path + [nums[i]], i + 1)

        dfs([], 0)
        return results

    def subsets_pyo(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # 선택하거나, 선택하지않거나
        def dfs(path, index):
            if index == len(nums):
                ans.append(path[:])
                return

            # 1. 선택 안 함
            dfs(path, index+1)
            # 2. 선택함
            dfs(path+[nums[index]], index+1)

        dfs([], 0)
        return ans

