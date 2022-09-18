# p221 Q16. 두 수의 덧셈
from typing import List

from ListNode import ListNode


class solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next

        return rev

    def List2num(self, head: ListNode) -> int:
        num = 0
        while head:
            num = num * 10 + head.val
            head = head.next

        return num

    def num2List(self, num: int, flag: bool) -> ListNode:  # reverse로 저장
        if flag == 0 and num == 0:
            return ListNode(0)
        if num > 0:
            return ListNode(num % 10, self.num2List(num // 10, 1))
        else:
            return None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1 = self.reverseList(l1)
        # l2 = self.reverseList(l2)
        # ans = self.num2List(self.List2num(l1) + self.List2num(l2))
        n1 = self.List2num(self.reverseList(l1))
        n2 = self.List2num(self.reverseList(l2))
        ans = self.num2List(n1+n2, 0)

        return ans
