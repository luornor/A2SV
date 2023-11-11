# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ksmallest = 0
        def smallest(root):
            if not root:
                return 
            #keep track of visisted nodes
            #call stack will start returning when we reach end of left tree
            smallest(root.left)
            self.count+=1
            if self.count == k:
                self.ksmallest = root.val
                
            smallest(root.right)

            return self.ksmallest
            
        return smallest(root)
        


        

        
        