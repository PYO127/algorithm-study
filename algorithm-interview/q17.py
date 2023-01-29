# p229 Q17. 페어의 노드 스왑
from typing import List

from ListNode import ListNode

class solution:
    def swapPairs_iter(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        curr = head
        prev.next = curr

        while curr and curr.next: # 노드 개수가 홀수개면 마지막 노드는 그대로 둠
            # 페어내부 스왑 + 다음 페어와 연결
            next = curr.next
            curr.next = next.next
            next.next = curr

            # 이전 페어와 연결
            prev.next = next

            curr = curr.next
            prev = prev.next.next

        return root.next

    def swapPairs_recur(self, head: ListNode) -> ListNode:
        curr = head
        if curr and curr.next:
            next = curr.next
            curr.next = self.swapPairs_recur(next.next)
            next.next = curr
            return next

        return head


