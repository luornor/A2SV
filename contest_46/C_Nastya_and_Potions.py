def solve():
    n,k = map(int,input().split())
    cost = list(map(int,input().split()))
    p = list(map(int,input().split()))

    for i in p:
        cost[i-1] = 0
    
    graph = [[] for _ in range(n)]
    indegree = [0]*n
    for i in range(n):
        l = list(map(int,input().split()))[1:]
        for j in l:
            graph[j-1].append(i)
            indegree[i] += 1
    
    res=[cost[i] if not indegree[i] else 0 for i in range(n)]
    ptr=0
    q=[i for i in range(n) if not indegree[i]]
    while ptr<len(q):
        i=q[ptr]
        res[i]=min(res[i],cost[i])
        for j in graph[i]:
            indegree[j]-=1
            res[j]+=res[i]
            if not indegree[j]:
                q.append(j)
        ptr+=1
    return res

for _ in range(int(input())):
    print(*solve())  