# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue = deque([root])
        
        graph = defaultdict(list)
        
        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.left].append(node)
                graph[node].append(node.left)
                queue.append(node.left)
            
            if node.right:
                graph[node.right].append(node)
                graph[node].append(node.right)
                queue.append(node.right)

        visited = set([target])
        res = []
        queue2 = deque([(target,0)])

        while queue2:
            node,level = queue2.popleft()

            if level>k:
                break

            if level==k:
                res.append(node.val)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue2.append((nei,level+1))
            
        return res

            