# p201 Q13. 팰린드롬 연결 리스트
import collections
from typing import List, Deque
from ListNode import ListNode


class solution:
    def isPalindrom_List(self, head: ListNode)->bool:
        q: List = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


    def isPalindrom_Deque(self, head: ListNode)-> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True


    def isPalindrom_runner(self, head: ListNode)->bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            # 연결리스트가 각각 홀수/짝수개로 이루어졌을 때 다 왔는지 판별
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            # 연결리스트가 홀수개로 이루어져있을 때, fast는 not None 이고,
            # slow 한 칸 더 전진시킨다.
            # 연결리스트(홀수) 가운데 값은 팰린드롬과 무관하므로
            slow = slow.next

        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next

        return not rev

