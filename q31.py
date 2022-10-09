# p307 Q31. 상위 K 빈도 요소
# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return list(zip(*freq.most_common(k)))[0]