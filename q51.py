# p428 Q51. 이진 탐색 트리(BST)를 더 큰 수 합계 트리로
from typing import List

from Node import TreeNode


class Solution:
    summation = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.bstToGst(root.right)
        self.summation += root.val
        root.val = self.summation
        self.bstToGst(root.left)

        return root
