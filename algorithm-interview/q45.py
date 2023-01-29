# p397 Q45. 이진 트리 반전
from typing import List

from Node import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return None

            right = dfs(node.left)
            left = dfs(node.right)

            node.left = left
            node.right = right

            return node

        return dfs(root)

