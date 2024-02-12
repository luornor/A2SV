from collections import deque

n, k = map(int, input().split())
walls = [input() for _ in range(2)]
dist = [[float('inf')] * (n+k) for _ in range(2)]

dist[0][0] = 0
q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    
    if dist[x][y] > y or walls[x][y] == 'X':
        continue
    
    if y + k >= n:
        print("YES")
        exit(0)
    
    for d in (-1, 0, 1):
        if 0 <= y + d < n and 1 + dist[x][y] < dist[x][y + d]:  # move up or down
            dist[x][y + d] = 1 + dist[x][y]
            q.append((x, y + d))
    
    if dist[1 - x][y + k] > 1 + dist[x][y]:  # jump (switches w between 0 and 1)
        dist[1 - x][y + k] = 1 + dist[x][y]
        q.append((1 - x, y + k))

print("NO")