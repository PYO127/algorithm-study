# p500 Q60. 삽입 정렬 리스트
from Node import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        curr = parent = ListNode(0)
        while head:
            while curr.next and curr.next.val < head.val:
                # input의 element 가 들어갈 위치를 앞에서부터 찾는다.
                # element가 크면 계속 다음 위치로
                # sorted linked list를 순회하다 element가 처음으로 작아질 때 반복 중단.
                curr = curr.next

            # 다중할당: 우변에 기존 값을 가지고 있고, 좌변에 차례대로 값을 바인딩.
            curr.next, head.next, head = head, curr.next, head.next
            # 들어가야할 위치 전후 연결 + 다음 unsorted 원소

            # 필요한 경우에만 curr가 처음(parent)으로 돌아가도록 처리
            if head and head.val < curr.next.val:
                curr = parent

        return parent.next



S = Solution()
S.insertionSortList(ListNode(3, ListNode(5, ListNode(4))))