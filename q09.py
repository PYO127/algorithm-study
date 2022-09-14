# p184 Q09. 세 수의 합
from typing import List

class solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums)-1):
            if i > 0 and nums[i-1] == nums[i]:
                # 중복된 값 건너뛰기
                continue

            # 간격을 좁혀 가며 sum 계산
            left, right = i+1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results

