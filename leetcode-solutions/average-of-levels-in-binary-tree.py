# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #first get the values at each level
        arr = [[]]
        if not root:
            return root

        queue = deque([(root,0)])
        # print(queue)
        while queue:
            node,level = queue.popleft()
            if level<len(arr):
                arr[level].append(node.val)
            else:
                arr.append([node.val])

            if node.left:
                queue.append((node.left,level+1))

            if node.right:
                queue.append((node.right,level+1))

        res = []
        #at each level calculate the average
        for level in arr:
            num_elements = len(level)
            sum_elements = sum(level)
            avg = sum_elements/num_elements
            res.append(avg)

        return res



        