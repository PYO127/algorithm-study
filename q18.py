# p233 Q18. 홀짝 연결 리스트
from typing import List

from ListNode import ListNode


class solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head

        return head

