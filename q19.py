# p237 Q19. 역순 연결 리스트
from typing import List

from ListNode import ListNode


class solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = start = ListNode(None)
        root.next = head
        for _ in range(m-1):
            start = start.next
        end = start.next

        for _ in range(n-m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        # 1. start, end 는 같은 노드에 고정
        # 2. tmp 는 start 다음으로 두고 -> iteration이 진행될 때 마다 start 다음 다음으로 이동
        # 3. start 다음은 end 다음 노드 & end 다음은 end 다음 다음 노드로 지정

        return root.next





