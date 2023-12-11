# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, running_total):
            nonlocal ans
            if not root:
                return 0
            # keep adding of node value
            running_total += str(root.val)
            # return val if at child node
            if not root.left and not root.right:
                ans += int(running_total)  # Add the running total to the answer

            left = dfs(root.left, running_total)
            right = dfs(root.right, running_total)

            return ans

        dfs(root, '')
        return ans

            
        