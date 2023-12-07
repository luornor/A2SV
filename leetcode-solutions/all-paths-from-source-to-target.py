class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(node,path,res):

            path.append(node)
            #if we are at the end of graph
            if node==len(graph)-1:
                res.append(path[:])

            for neighbour in graph[node]:
                dfs(neighbour,path,res)
            
            #remove from list at the end
            path.pop()

        res = []
        dfs(0,[],res)

        return res
 