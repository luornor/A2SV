t = int(input())

def simulate_fall(grid):
    rows,cols = len(grid), len(grid[0])
    # occupied = [[False]*cols for _ in range(rows)]
    # move through each column from left to right
    for c in range(cols):
        #move through each row from buttom to top except last row
        for r in range(rows-1,-1,-1):
            #if we find a stone
            #we loop through the column from buttom to top row
            # and let the stone fall
            for i in range(rows-2,-1,-1):
                while grid[i][c] == '*' and grid[i+1][c]=='.':
                    grid[i][c]= '.'
                    grid[i+1][c]='*'
    
    return grid



for _ in range(t):
    rows,cols = map(int,input().split()) # Read the number of rows and columns
    grid = [list(input()) for _ in range(rows)]   # Read the input grid
    #simulate the fall process
    grid = simulate_fall(grid)

    #output the grid
    for row in grid:
        print(''.join(row))
    if _!= t-1:
        print()

