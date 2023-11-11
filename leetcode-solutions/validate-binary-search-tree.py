# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root,min_val,max_val):
            if not root:
                return True

            #all node to left are less than it
            if not(min_val<root.val<max_val):
                return False
            # root now becomes maximum value for left tree
            #every number at left is minimum
            left_tree = isvalid(root.left,min_val,root.val)
            # root now becomes min value for right tree
            #every number at right is maximum
            right_tree = isvalid(root.right,root.val,max_val)

            return left_tree and right_tree

        return isvalid(root,float('-inf'),float("inf"))




        
        