# p390 Q43. 이진 트리의 직경
from typing import List

from Node import TreeNode


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(Node: TreeNode):
            # 노드가 없을 경우
            if not Node:
                return -1
            left = dfs(Node.left)
            right = dfs(Node.right)

            self.longest = max(self.longest, left+right+2)
            # 리턴으로 뱉는 값은 리프 노드에서 현재노드까지의 거리
            return max(left, right)+1

        dfs(root)
        return self.longest

