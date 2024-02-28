from collections import defaultdict
def solve():
    n = int(input())
    graph = defaultdict(list)

    for _ in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    child_count = defaultdict(int)
    
    visited = set() 
    saved_vertices = 0
    print(graph)
    #to choose or not to choose
    def dfs(current_node):
        nonlocal saved_vertices
        
        visited.append(current_node)
        

        for nei in graph[current_node]:
            #pick or don't pick
            if nei not in visited:
                max(dfs(nei,True) , dfs(nei,False))

        return saved_vertices
    
    dfs(1,None)

    return saved_vertices


t =int(input())
for _ in range(t):
    print(solve())
    

