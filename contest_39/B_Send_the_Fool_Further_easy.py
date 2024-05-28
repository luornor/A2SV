
n = int(input())
graph = {i: [] for i in range(n)}

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

max_cost = 0
visited = set()
def dfs(node, cost):
    max_cost = cost 
    visited.add(node)
    for neighbor, nei_cost in graph[node]:
        if neighbor not in visited:
            max_cost = max(max_cost, dfs(neighbor, cost + nei_cost))
    return max_cost

max_cost = dfs(0, 0)
print(max_cost)