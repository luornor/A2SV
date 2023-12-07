# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ''
        def dfs(root):
            nonlocal ans
            if not root:
                return ''
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left and right:
                ans = f'{root.val}({left})({right})'
            elif left:
                ans = f'{root.val}({left})'
            elif right:
                ans = f'{root.val}()({right})'
            else:
                ans = f'{root.val}'
        
            return ans

        return dfs(root)
        


