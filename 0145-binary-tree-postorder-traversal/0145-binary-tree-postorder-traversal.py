# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def helpingFunction(node):
            if not node:
                return output
            helpingFunction(node.left)
            helpingFunction(node.right)
            output.append(node.val)
            

        helpingFunction(root)
        return output