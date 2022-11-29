# p387 Q42. 이진 트리의 최대 깊이
from collections import deque
from Node import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = deque([root])
        depth = 0
        if root is None:
            return 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                # 부모 노드가 있는 큐에 들어가는 것이
                # 위험해보일 수도 있으나,
                # 처음에 len(queue)로 부모 노드의 길이만큼
                # 반복하도록 선언했으므로 문제없다.
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
