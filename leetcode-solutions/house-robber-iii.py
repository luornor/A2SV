# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #iterative dfs for bottom up
        
        def dp(root):
            if root is None:
                return [0,0]
            

            left = dp(root.left)
            right = dp(root.right)

            res =[]
            #root included
            res.append(root.val+ left[1] + right[1])

            #root excluded
            res.append(max(left)+max(right))
            
            return res

        return max(dp(root))

        

        