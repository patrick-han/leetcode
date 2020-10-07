# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recrusive Solution
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



    # Iterative solution
    def isBalancedIter(self, root: TreeNode) -> bool:
        # DFS, postorder
        height_dict = {None:0} # Place this in the dict for when we reach a leaf node, we want to say we know the height of the None "branches"
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                if cur.left in height_dict and cur.right in height_dict:
                    left_height = height_dict[cur.left]
                    right_height = height_dict[cur.right]
                    if abs(left_height - right_height) > 1: # If the height differences of the left and right branches are > 1
                        return False
                    else:
                        height_dict[cur] = max(left_height, right_height) + 1 # Store the max depth of the current node taking the max of left,right branches
                else:
                    # Reach here if we haven't calculated the height for one of the branches
                    # Post order is: left->right->root so left goes on the the top of the stack
                    stack.append(cur)
                    stack.append(cur.right)
                    stack.append(cur.left)
        return True