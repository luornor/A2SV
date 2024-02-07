
from collections import defaultdict, deque


def solve():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    graph = defaultdict(list)
    for _ in range(n):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([(1)])
  
    

t = int(input())
for i in range(t):
    if t[i]!='':
        print(solve())