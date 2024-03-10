from collections import defaultdict
        
def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    colors = [0]+list(map(int,input().split()))

    memo = {}
    def dfs(node,parent):
        if (node, parent) in memo:
            return memo[(node, parent)]
        
        for child in graph[node]:
            if child != parent:
                memo[(child, node)] = dfs(child, node)
                if colors[child] != colors[node] or not memo[(child, node)]:
                    return False
        return True
             

    for i in range(1,n+1):
        possible = True
        for child in graph[i]:
            possible &= dfs(child, i)

        if possible:
            return f'YES\n{i}'

                
    return 'NO'

print(solve())