# p245 Q20. 유효한 괄호
from typing import List


class solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
