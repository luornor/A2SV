# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(root,currsum):
            if not root:
                return 

            currsum+=root.val
            #when u get to a child node
            if not root.left and not root.right:
                return currsum==targetSum

            return path(root.left,currsum) or  path(root.right,currsum)

            
        if root:
            return path(root,0)
        else:
            return False
        

            

        
        