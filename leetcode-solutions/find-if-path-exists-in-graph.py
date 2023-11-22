class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])            
            
        # print(graph)

        visited = set()
        def dfs(current,visisted):
            
            if current in visited:
                return False

            if current==destination:
                return True
        
            visited.add(current)
            for num in graph[current]:
                if dfs(num,visited):
                    return True

            return False

        return dfs(source,visited)

