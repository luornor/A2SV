
from collections import defaultdict
import heapq


n,m = map(int,input().split())
graph = defaultdict(list)

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

queue = [1]
ans = []

heapq.heapify(queue)
visited = set()
visited.add(1)

while queue:
    node = heapq.heappop(queue)

    ans.append(node)

    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            heapq.heappush(queue,nei)


print(*ans)
            
