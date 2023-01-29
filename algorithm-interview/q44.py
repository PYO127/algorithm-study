# p393 Q44. 가장 긴 동일 값의 경로

from Node import TreeNode


class Solution:
    largest = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node: TreeNode):
            if not node:
                return 0
            # left, right 는 자식 노드가 그들의 자식 노드로부터
            # 연속된 동일 값의 개수를 체크
            left = dfs(node.left)
            right = dfs(node.right)

            color = node.val

            if node.left and node.left.val == color:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == color:
                right += 1
            else:
                right = 0

            self.largest = max(self.largest, left+right)

            return max(left, right)
            # 현재 노드의 부모 노드는 현재 노드의 양쪽 자식 노드와
            # 동시에 경로를 생성할 수 없다. 따라서 현재 노드의 양 쪽 자식 노드 중 큰 상태값(동일값 경로의 길이)을 갖는 노드를 택하는 것이 맞다.
        dfs(root)
        return self.largest












