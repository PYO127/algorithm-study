# p213 Q14. 두 정렬 리스트의 병합
from typing import List

from ListNode import ListNode

class solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        # 백트래킹
        if (not l1) or (l2 and l1.val > l2.val):
            # l1.val > l2.val
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1