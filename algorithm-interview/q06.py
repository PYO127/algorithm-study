# p159 Q06. 가장 긴 팰린드롬 부분 문자열
from typing import List


class solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
            # left+1 로 원위치, right-1 하지 않는 이유? -> slicing 주의

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),  # abba 같은 팰린드롬
                         expand(i, i + 2),  # abcba 같은 팰린드롬
                         key=len)

        return result
