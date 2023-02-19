# p504 Q61. 가장 큰 수
from typing import List


class Solution:
    def to_swap(self, n1: int, n2: int) -> bool:
        # 예를 들면, n1 = 10, n2 = 2 일 때,
        # '102', '210' 둘 중 어떤 것이 더 큰 수 인지 체크하기 위해 만든 메소드
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        i = 1  # 삽입 정렬 에서 첫 번째 원소는 이미 정렬되어 있으므로 i = 1 부터 시작
        while i < len(nums):
        # 삽입 정렬에 대한 설명은 아래 링크(Q60) 참고
        # https://leetcode.com/problems/insertion-sort-list/description/
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):                
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1

        # nums가 모두 0으로 이루어진 경우 결과가 '000' 이 될 수 있으므로 아래와 같이 처리
        return str(int(''.join(map(str, nums))))
