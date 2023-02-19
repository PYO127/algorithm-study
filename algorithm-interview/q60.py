# p500 Q60. 삽입 정렬 리스트
from Node import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = parent = ListNode(None)
        while head:
            while curr.next and curr.next.val < head.val:
                curr = curr.next

            # 다중할당: 우변에 기존 값을 가지고 있고, 좌변에 차례대로 값을 바인딩.
            curr.next, head.next, head = head, curr.next, head.next

            # 필요한 경우에만 curr가 처음(parent)으로 돌아가도록 처리
            if head and head.val < curr.next.val:
                curr = parent

        return parent.next
