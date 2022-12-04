# p413 Q48. 균형 이진 트리
from Node import TreeNode


class Solution:
    flag = True

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node: TreeNode) -> int:
            # if node is not 쓰면 안될까?
            if node and self.flag:
                d_l = dfs(node.left)
                d_r = dfs(node.right)
                if abs(d_l - d_r) > 1:
                    self.flag = False
                return max(d_l, d_r) + 1
            return 0

        dfs(root)
        return self.flag



