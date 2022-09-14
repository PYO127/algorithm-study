# p219 Q15. 역순 연결 리스트
from typing import List

from ListNode import ListNode


class solution:
    def reverseList_iter(self, head:ListNode) -> ListNode:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next

        return rev

    def reverseList_recur(self, head:ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)