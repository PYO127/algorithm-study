# p425 Q50. 정렬된 배열의 이진 탐색 트리 변환
from typing import List
from Node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2  # 버림

        node = TreeNode(nums[mid],
                        self.sortedArrayToBST(nums[:mid]),    # 0 to mid-1
                        self.sortedArrayToBST(nums[mid+1:]))  # mid+1 to len(nums)-1

        return node
