from collections import deque
def solve():
    n, m, k = map(int, input().split())
    maze = [[None for _ in range(m)] for _ in range(n)]
    
    start = None
    total = 0
    for i in range(n):
        s = list(input())
        for j in range(m):
            if s[j]=='.':
                maze[i][j]='X'
                start = (i,j)
                total+=1
            else:
                maze[i][j]=s[j]

    
    
    queue = deque()
    queue.append(start)
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
   
    count = 0

    while queue:
        x, y = queue.popleft()
        if i<0 or i>=n or j<0 or j>=m or count==total-k:
            continue
        
        if maze[x][y] == 'X':
            maze[x][y] = '.'
            count += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m :
                queue.append((nx, ny))

       
    

    for row in maze:
        print(''.join(row))


solve()