# p444 Q54. 전위, 중위 순회 결과로 이진 트리 구축
from typing import List, Optional
from Node import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder 의 제일 처음은 root
        if inorder:
            index = inorder.index(preorder.pop(0))

            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])  # 0 부터 index-1 까지
            root.right = self.buildTree(preorder, inorder[index+1:])  # index+1 부터 끝까지

            return root
