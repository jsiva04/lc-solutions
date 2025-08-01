# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            print("neither")
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            print("p: " + str(p.val) + ", q: " + str(q.val))
            if p.val != q.val:
                return False
            else:
                return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))