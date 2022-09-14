# p190 Q10. 배열 파티션 1
from typing import List


class solution:
    def arrayPairSum_0(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()

        for i, num in enumerate(nums):
            if i % 2 == 1:
                continue
            ans += num

        return ans

    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
