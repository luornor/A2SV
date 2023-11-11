# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(a,b):
            if not a and not b:
                return True
            
            if not a or not b:
                return False

            #recurse if the values are the same
            if a.val==b.val:
                #for mirror left is equal to right and vice versa
                left_call = isMirror(a.left, b.right) 
                right_call = isMirror(a.right, b.left)
                return left_call and right_call

            else:
                return False
        
        return isMirror(root.left, root.right)

            
        