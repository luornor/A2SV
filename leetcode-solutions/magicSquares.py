import collections
def numMagicSquaresInside(grid: list[list[int]]) -> int:
    rows,cols = len(grid),len(grid[0])
    count = 0       
    for r in range(rows-2):
        for c in range(cols-2):
            if Ismagic_square(grid,r,c):
                count+=1
    
    return count
def Ismagic_square(grid,start_row,start_col):
        #row sum
        row_sum = sum(grid[start_row][start_col:start_col+3])

        hmap = collections.defaultdict(set)
        # Check for distinct numbers and range validity
        for i in range(start_row,start_row+3):
            for j in range(start_col,start_col+3):
                if grid[i][j] in hmap[i] or grid[i][j] not in range(1,10):
                    return False
                hmap[i].add(grid[i][j])
                #if all row sum is equal
                if sum(grid[i][start_col:start_col+3]) !=row_sum:
                    return False
                #if row is equal to all columns
                if sum(grid[start_row][j] for start_row in range(start_row,start_row+3))!=row_sum:
                    return False
        #check each row each coloumn , each diagonal , each reverse diagonal
        diagonal_sum =grid[start_row][start_col]+ grid[start_row+1][start_col+1]+grid[start_row+2][start_col+2]
        reverse_diagonal_sum = grid[start_row][start_col+2]+ grid[start_row+1][start_col+1]+grid[start_row+2][start_col]
        if diagonal_sum!= row_sum or reverse_diagonal_sum!= row_sum:
                return False
        
        return True



    
            

print(numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
                
