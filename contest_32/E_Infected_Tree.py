from collections import defaultdict
def solve():
    n = int(input())
    graph = defaultdict(list)

    for _ in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    infected = [False]*(n+1)
    saved_vertices = 0

    def dfs(current_node,parent):
        nonlocal saved_vertices

        infected[current_node]=True

        for nei in graph[current_node]:
            #if neighbour is not infected
            if not infected[nei] and nei != parent:
                dfs(nei,current_node)

        saved_vertices+=1
    
    dfs(1,None)

    return saved_vertices


t =int(input())
for _ in range(t):
    print(solve())
    

