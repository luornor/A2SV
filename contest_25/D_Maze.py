def solve():
    n, m, k = map(int, input().split())
    grid = []
    for _ in range(n):
        s = input()
        grid.append(list(s))

    start_x, start_y = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                start_x, start_y = i, j
                break
        if start_x != -1:
            break

    visited = set()
    def dfs(x, y):
        nonlocal k
        k -= 1
        if k == 0:
            return
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != '.':
            return
        
        if (x,y) not in visited:
            grid[x][y] = 'X'
            visited.add((x,y))
        
        
        dfs(x + 1, y)  
        dfs(x - 1, y)  
        dfs(x, y + 1)  
        dfs(x, y - 1)  

    dfs(start_x, start_y)

    for row in grid:
        res = ''.join(row)
        print(res)


solve()