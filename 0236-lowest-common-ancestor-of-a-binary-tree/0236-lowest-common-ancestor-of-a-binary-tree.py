# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       # Base case: if root is null or root is one of the target nodes, return root
        if not root or root == p or root == q:
            return root
        
        # Recursively search for p and q in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are not null, it means p and q are found in different subtrees,
        # so the current root is the LCA
        if left and right:
            return root
        
        # Otherwise, return the non-null child (either left or right)
        return left if left else right 