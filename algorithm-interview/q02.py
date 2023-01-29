# p145 Q02. 문자열 뒤집기
from typing import List

class solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString_reveres(self, s: List[str])-> None:
        return s.reverse()
