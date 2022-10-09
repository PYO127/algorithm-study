# p291 Q28. 해시맵 디자인
# https://leetcode.com/problems/design-hashmap/
import collections
from typing import List

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        # default 값을 ListNode(None, None) 으로 생성

    def put(self, key: int, value: int) -> None:
        index = key % self.size # 모듈로, 나머지 연산
        if self.table[index].value is None:
            # defaultdict로 생성하면, 조회할 때 값이 뭘로 들어가나?
            self.table[index] = ListNode(key, value)
        else: # 해시 충돌 발생
            node = self.table[index]
            while node:
                #  1. 이미 해당 키 값이 존재 -> value 업데이트
                if node.key == key:
                    node.value = value
                    return
                if node.next is None:
                    break
                node = node.next
            # 2. 해당 키 값 미존재 -> 개별 체이닝 구현
            node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1


    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        # 1. 인덱스의 첫 번째 노드일 때 삭제 방법
        node = self.table[index]
        if node.key == key:
            self.table[index] = ListNode() if node.next is None else node.next
            return
            # None이 아닌, ListNode() 로 세팅하는 이유
            # : 조회, 추가, 삭제 모두 처음에 self.table[index].value is None 으로
            # 해당 인덱스에 노드가 존재하는지 확인하는데, 만약 None으로 변경해버리면,
            # 이 부분에서 오류가 발생할 수 있다.
        # 2. 연결리스트 중간 노드일 때 삭제 방법
        # prev 를 어떻게 두어야할지 상당히 고민했는데, (*) 처럼 두어도 될까?
        # 정답은 yes. 왜냐하면, 이미 1. 에서 인덱스의 첫 번째 노드인 경우에 대해 처리를 해둔 상황
        # 따라서 while 문에 들어가고 첫번째는 바로 (**) 로 가게될 것
        prev = node # (*)
        while node:
            if node.key == key:
                prev.next = node.next
                return
            prev, node = node, node.next  # (**)






class MyHashMap2:
    # 단순히 딕셔너리 이용
    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key] if key in self.map else -1

    def remove(self, key: int) -> None:
        if key in self.map:
            self.map.pop(key)


