# p431 Q52. 이진 탐샘 트리(BST) 합의 범위
from collections import deque
from typing import List
from Node import TreeNode


class Solution:
    cnt = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def dfs(node: TreeNode):
            if not node:
                return 0
            # 1. low 보다 작은 경우
            if node.val < low:
                return dfs(node.right)
            # 2. high 보다 큰 경우
            if node.val > high:
                return dfs(node.left)
            # 3. low < val < high 인 경우
            return node.val + dfs(node.left) + dfs(node.right)

        def bfs():
            queue = deque()
            queue.append(root)
            ans = 0
            while queue:
                node = queue.popleft()
                if low < node.val:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    ans += node.val

            return ans




        return dfs(root)


