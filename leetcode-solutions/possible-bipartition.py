class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        #Assign a color to each vertex of a graph in 
        #such a way that no two adjacent vertices have the same color.
        graph = defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [-1]*(n+1)
        def dfs(node):
            for neighbour in graph[node]:
                #already coloured
                if color[neighbour]!=-1:
                    if color[node]==color[neighbour]:
                        return False
                else:
                    #uncoloured
                    color[neighbour] = 1 - color[node]
                    if not dfs(neighbour):
                        return False

            return True


        for node in range(1,n+1):
            #not colored
            if color[node]==-1:
                color[node]=0
                if not dfs(node):
                    return False

        return True
        