# p180 Q08. 빗물 트래핑
from typing import List


class solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        # height 중 가장 높은 위치를 기준으로 left, right 두 포인터가 좁혀져오는 방식
        while left < right:
            left_max, right_max = max(left_max, height[left]), \
                                  max(right_max, height[right])
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume
