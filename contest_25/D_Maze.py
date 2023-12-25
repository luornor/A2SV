from collections import deque
def solve():
    n, m, k = map(int, input().split())
    maze = []
    for _ in range(n):
        s = input()
        maze.append(list(s))

    
    start = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '.':
                start = (i,j)
                break
        if start:
            break
        
    visited = set(start)
    queue = deque([start])
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    count = 0

    while queue and count < k:
        x, y = queue.popleft()

        if maze[x][y] == '.':
            maze[x][y] = 'X'
            count += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '.' and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
    
    # for i in range(n):
    #     for j in range(m):
    #         if maze[i][j] == '.':
    #             maze[i][j] = '.'
    #         elif maze[i][j] == 'X':
    #             maze[i][j] = 'X'
    #         else:
    #             maze[i][j] = '#'

    for row in maze:
        res = ''.join(row)
        print(res)


solve()