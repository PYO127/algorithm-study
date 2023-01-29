# p138 Q01. 유효한 팰린드롬
import collections
import re
from typing import List, Deque


class solution:
    def isPalindrome_list(self, s: str) -> bool:
        strs = []
        # 전처리: 특수문자, 공백 제거 및 lowercase 변환
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 펠린드롬 여부 판별
        while len(strs) > 1:
            # list pop(0)는 O(n)
            if strs.pop(0) != strs.pop():
                return False

        return True

    def isPalindrome_deque(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            # deque의 popleft()는 O(1)
            if strs.popleft() != strs.pop():
                return False

        return True

    def isPalindrome_slicing(self, s:str) -> bool:
        s = s.lower()
        # 정규표현식 사용
        s = re.sub('[^a-z\d]', '', s)

        # 문자열 뒤집기
        return s == s[::-1]

