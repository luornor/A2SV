class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited= set()
        def dfs(r,c):
            # Out of bounds
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 
            if grid[r][c]=='0' or (r,c) in visited:
                return
            visited.add((r,c))
            # grid[r][c] =='0'

            dfs( r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs( r, c + 1)  # Right

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i, j) not in visited:
                    dfs(i,j)
                    count+=1


        return count
        