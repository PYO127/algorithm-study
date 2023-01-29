# p274 Q27. K개 정렬 리스트 병합
# https://leetcode.com/problems/merge-k-sorted-lists/
import heapq
from typing import List
from ListNode import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            Node = heapq.heappop(heap)
            idx = Node[1]
            result.next = Node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

