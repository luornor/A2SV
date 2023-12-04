from collections import defaultdict


def solve():
    n = int(input())
    nodes = list(map(int,input().split()))
    s = input()
    graph = {i+1: [] for i in range(n)}
    for i in range(n-1):
        graph[nodes[i]].append(i+2)

    visited = set()
    res=0
    w_count = 0
    b_count = 0
    def dfs(node):
        nonlocal res,w_count,b_count
        visited.add(node)
        if w_count==b_count:
            res+=1
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)
                if s[neighbour-1]=='b':
                    b_count+=1
                else:
                    w_count+=1
        
        return res
    
    for i in range(1,n+1):
        if i not in visited:
            return dfs(i)






t = int(input())
for _ in range(t):
    print(solve())