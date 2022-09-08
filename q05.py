# p153 Q05. 그룹 애너그램
import collections
from typing import List


class solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            # 정렬된 문자열을 키로, 그 value 로 정렬 이전 값들의 리스트
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())

