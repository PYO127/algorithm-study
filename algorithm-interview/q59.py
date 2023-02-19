# p497 Q59. 구간 병합
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for intvl in intervals:
            if merged and intvl[0] <= merged[-1][1]:  # 직전에 추가했던 구간의 끝보다 추가할 구간의 시작이 작은 경우
                merged[-1][1] = max(merged[-1][1], intvl[1])
            else:
                merged.append(intvl)
                # merged += intvl,
                # merged += [intvl]

        return merged
