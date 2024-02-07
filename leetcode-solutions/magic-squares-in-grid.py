class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check_squares(r,c):
            primary = grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2]
            secondary = grid[r][c+2]+grid[r+1][c+1]+grid[r+2][c]
            row_sum = sum(grid[r][c:c+3])
            #distinct numbers
            unique = set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] in unique or grid[i][j] not in range(1,10):
                        return False
                    unique.add(grid[i][j])
                    #rows
                    if sum(grid[i][c:c+3]) !=row_sum:
                        return False
                    #cols
                    col_sum = 0
                    for x in range(r,r+3):
                        col_sum+=grid[x][j]
                    
                    if col_sum!=row_sum:
                        return False

            if primary!=row_sum or secondary!=row_sum:
                return False

            return True
                        
        def is_valid(r,c):
            return 0<=r <len(grid) and 0<= c <len(grid[0])
        count = 0
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                if is_valid(r,c) and check_squares(r,c):
                    count+=1


        return count 



            
                


        