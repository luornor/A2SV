class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])            
            
        # print(graph)

        visited = set()
       
        def dfs(current,visisted):
            
            if len(graph[current])==len(graph.keys())-1:
                return current

            visited.add(current)
            for num in graph[current]:
                if num not in visited:
                    return dfs(num,visited)

        return dfs(edges[0][0],visited)
        # for k,v in graph.items():
        #     if len(v)==len(graph.keys())-1:
        #         return k
        