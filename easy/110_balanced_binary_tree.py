# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int:
    depths = []

    def depth(root, max_depth):
        if not root:
            depths.append(max_depth)
        else:
            max_depth += 1
            depth(root.left, max_depth)
            depth(root.right, max_depth)

    depth(root, 0)
    return(max(depths))

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if abs(maxDepth(self, root.left) - maxDepth(self, root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)