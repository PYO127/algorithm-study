# p489 Q58. 정렬
from Node import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        # 런너 기법: 분할정복을 을 위해 가운데 찾으려고 사용
        half, slow, fast = None, head, head
        while fast and fast.next:
            # 전체 리스트의 길이가 짝수면 마지막에 fast는 None,
            # 홀수면 리스트 마지막 노드가 되므로,
            # while 조건을 위와 같이 사용
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
        # half가 왼쪽 리스트 마지막 노드,
        # slow가 오른쪽 리스트 첫 번째 노드가 된다.
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)

    # 두 정렬 리스트 병합: left, right 는 각각 이미 정렬 되어있는 상태
    def mergeTwoLists(self, left: ListNode, right: ListNode) -> ListNode:
        if left and right:
            if left.val > right.val:
                left, right = right, left
            left.next = self.mergeTwoLists(left.next, right)

        # 단락 평가: left에 값이 있으면 항상 left,
        # left 가 none 이면 right를 리턴
        return left or right
