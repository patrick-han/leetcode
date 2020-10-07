# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = {} # Memoization for the depth calculations
        
    def maxDepth(self, node): # Helper function that finds the max height in a subtree
        if (not node):
            return 0
        if (node in self.d): # Return memoized depth calculation
            return self.d[node]
        else:
            self.d[node] =  1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
            return self.d[node]
        
    def isBalanced(self, root: TreeNode) -> bool:
        # A tree is balanced if abs(height(left)-height(right)) <= 1
        if (not root):
            return True
        
        offByOneOrLess = abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1
        return offByOneOrLess and self.isBalanced(root.left) and self.isBalanced(root.right)