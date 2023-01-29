# p435 Q53. 이진 탐색 트리 (BST) 노드 간 최소 거리
import sys
from Node import TreeNode


class Solution:
    result = sys.maxsize
    prev = -sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        # BST 에서 중위 순회 -> prev의 val가 항상 현재노드의 val보다 작아서
        # root.val - self.prev 가 음수가 될 수 없다.

        if root.right:
            self.minDiffInBST(root.right)

        return self.result