# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
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