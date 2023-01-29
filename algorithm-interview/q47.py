# p406 Q47. 이진 트리 직렬화 & 역직렬화
from collections import deque
from typing import List

from Node import TreeNode


class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ''
        q = deque()
        q.append(root)
        result = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))

            else:
                result.append('#')

        return ' '.join(result)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        vals = data.split()
        root = TreeNode(int(vals[0]))
        # q = deque(root) 안되는 이유? -> iterable 을 파라미터로 받음
        q = deque([root])
        idx = 1  # 리스트 vals 용 idx
        while q:
            node = q.popleft()
            # 왜 != 가 아닌 is not 으로 하는지?
            if vals[idx] != '#':
                node.left = TreeNode(int(vals[idx]))
                q.append(node.left)
            idx += 1
            if vals[idx] != '#':
                node.right = TreeNode(int(vals[idx]))
                q.append(node.right)
            idx += 1

        return root
