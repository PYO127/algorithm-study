# p257 Q24. 스택을 이용한 큐 구현
# https://leetcode.com/problems/implement-queue-using-stacks/
from typing import List

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        # s2 가 비어있을 때만 s1 -> s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            # while문 지나고 나면 s1은 empty
        return self.s2[-1]

    def empty(self) -> bool:
        return not len(self.s1) and not len(self.s2)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()