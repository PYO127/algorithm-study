# p173 Q07. 두 수의 합
from typing import List


class solution:
    def twoSum0(self, nums: List[int], target: int)-> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                # i = nums_map[num] 이므로 i = nums_map[target-num] 이 될 경우, target = num + num
                return [i, nums_map[target-num]]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        # twoSum0 구조 개선
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i