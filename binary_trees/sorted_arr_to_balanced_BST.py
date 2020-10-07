# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildSubTree(left, right):
            if (left > right): # When we try to build a sub tree for a leaf node
                return None
            mid = (left + right) // 2
            midNode = TreeNode(nums[mid]) # The middle node of the sub array is always > left and <= right since we've sorted the array
            midNode.left = buildSubTree(left, mid - 1)
            midNode.right = buildSubTree(mid + 1, right)
            return midNode
        return buildSubTree(0, len(nums) - 1) # Pass indexes instead of sliced arrays, slicing arr is an expensive operation