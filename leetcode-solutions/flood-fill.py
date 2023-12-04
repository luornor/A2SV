class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(grid,color,r,c,original_color):
            # Out of bounds or different color
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != original_color or grid[r][c]==color:
                return grid

            grid[r][c] = color

            dfs(grid, color, r - 1, c,original_color)  # Up
            dfs(grid, color, r + 1, c,original_color)  # Down
            dfs(grid, color, r, c - 1,original_color)  # Left
            dfs(grid, color, r, c + 1,original_color)  # Right

            return grid

        original_color = image[sr][sc]
        return dfs(image,color,sr,sc,original_color)
        