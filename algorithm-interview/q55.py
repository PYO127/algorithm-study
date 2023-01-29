# p456 Q55. 배열의 K번째 요소
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        # 1. heap에 insert
        # heapq 모듈은 최소힙만 지원한다.
        # 하지만, 음수로 저장한 다음, 가장 낮은 수 추출 후
        # 부호를 바꾸면 최대힙처럼 동작 가능하다.
        for n in nums:
            heapq.heappush(heap, -n)

        # 2. k-1번 추출
        for _ in range(1,k):
            heapq.heappop(heap)

        # 3. k번째 큰 원소 추출
        return -heapq.heappop(heap)
