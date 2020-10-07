# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, node): # Helper function that finds the max height in a subtree
        if (not node):
            return 0
        else:
            return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
        
    def isBalanced(self, root: TreeNode) -> bool:
        # A tree is balanced if abs(height(left)-height(right)) <= 1
        if (not root): # Base case, an empty node is "balanced"
            return True
        elif (abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1): # Sub problem to solve if the two subtrees are balanced
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) # Recursive call to both subtrees