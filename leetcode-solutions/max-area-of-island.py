class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(r,c,count):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                return 0
            if grid[r][c]==0 or (r,c) in visited:
                return 0

            visited.add((r,c))
            count=1

            # grid[r][c]=0
            count+=dfs(r-1,c,count)
            count+=dfs(r+1,c,count)
            count+=dfs(r,c-1,count)
            count+=dfs(r,c+1,count)
            
            return count
            
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    area = max(area,dfs(i,j,area))

        return area
        