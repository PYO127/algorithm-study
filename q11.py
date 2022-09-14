# p193 Q11. 자신을 제외한 배열의 곱
from typing import List

class solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        out = []
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums)-1, 0-1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out



