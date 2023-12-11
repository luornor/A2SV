
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}

        if not node:
            return

        def dfs(original):
            if original in graph:
                return graph[original]

            #new node
            new_node= Node(original.val)

            #copy of original node
            graph[original]=new_node

            for neighbour in original.neighbors:
                new_neighbor = dfs(neighbour)
                new_node.neighbors.append(new_neighbor)
                    
            return new_node


        return dfs(node)

            
            
        