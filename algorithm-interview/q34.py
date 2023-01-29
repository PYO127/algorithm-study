# p341. Q34. 순열
# https://leetcode.com/problems/permutations/
from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                # 반드시 값은 복사하는 형태로 사용
                # 그렇지 않으면 prev_elements 가 변경될 경우, ans의 원소도 함께 변경
                ans.append(prev_elements[:])

            for e in elements:
                # 복사
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return ans


    def permute_itertools(self, nums:List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))
        # return list(itertools.permutations(nums))
        # 아래처럼 할 경우 결과 형식이 List[Tuple[int]] 로 나온다.