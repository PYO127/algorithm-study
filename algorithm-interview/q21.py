# p247 Q21. 중복 문자 제거
import collections
from typing import List


class solution:
    def removeDuplicateLetters_recursive(self, s: str) -> str:
        for char in sorted(set(s)):
            # set 출력해보면 순서가 멋대로 나옴 -> sorted 필수
            suffix = s[s.index(char):]
            if set(suffix) == set(s):
                # set '==': 원소가 모두 일치
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


    def removeDuplicateLetters_stack(self, s: str) -> str:
        stack = []
        seen = set()
        counter = collections.Counter(s)

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 스택 가장 위보다 앞선 알파벳 등장 + 스택 가장 위 알파벳이 뒤에도 존재
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

