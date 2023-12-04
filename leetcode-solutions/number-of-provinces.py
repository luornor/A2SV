class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def dfs(node):
            if not graph[node]:
                return 
            if node not in visited:
                visited.add(node)
            else:
                return
            for neighbor in graph[node]:
                dfs(neighbor)

            
        
        graph = {i+1:[] for i in range(len(isConnected))}
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]== 1 and i!=j:
                    graph[i+1].append(j+1)
        # print(graph)
        count=0
        for key,val in graph.items():
            if key not in visited:
                dfs(key)
                count+=1
        return count
         

