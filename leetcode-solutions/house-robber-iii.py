# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(root):
            if root is None:
                return 0
            
            if root in memo:
                return memo[root]

            #when we chose to rob starting from the root
            rob = root.val
            if root.left:
                rob += dp(root.left.left) + dp(root.left.right)
            if root.right:
                rob += dp(root.right.left) + dp(root.right.right)

            #when we skip the root and rob connected nodes
            skip = dp(root.left) + dp(root.right)
            #find max between the two
            memo[root] = max(rob, skip)
            return memo[root]

        return dp(root)

        