# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def LCA(root,p,q):
            if not root:
                return 
            #if p is less than root node search left tree
            left_part=None
            right_part=None
            if root.val>p.val and root.val> q.val:
                left_part = LCA(root.left,p,q)
            #if q is less than root node search right tree
            elif root.val<p.val and root.val<q.val:
                right_part = LCA(root.right,p,q)

            else:
                return root

            return left_part or right_part

            
            

        return LCA(root,p,q)

            

            

        