class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        sums = []
        val = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                val=grid[i][j]+grid[i+1][j+1]+grid[i-1][j-1]+grid[i-1][j+1]+grid[i+1][j-1] + grid[i+1][j] + grid[i-1][j]
                sums.append(val)
        return max(sums)
                