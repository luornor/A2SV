def xSum(board):
    max_sum = 0
    row = len(board) # rows
    col = len(board[0]) #cols
    # For each cell at position (i, j), 
    # calculate the sum of all cells attacked by a bishop placed at that position.
    # sum_attacked = 0
    for i in range(row):
        for j in range(col):
            # the value of the current cell
            sum_attacked = board[i][j]
            
            # check up-left diagonal
            x,y = i,j
            while x>0 and y>0:
                x-=1
                y-=1
                sum_attacked+=board[x][y]
                
            #check up-right diagonal
            x,y = i, j
            while x>0 and y<col-1:
                x-=1
                y+=1
                sum_attacked+=board[x][y]
                
            #check down-left diagonal
            x,y = i, j
            while x<row-1 and y>0:
                x+=1
                y-=1
                sum_attacked+=board[x][y]
                
            #check down-right diagonal
            x,y = i, j
            while x<row-1 and y<col-1:
                x+=1
                y+=1
                sum_attacked+= board[x][y]
                
                
            max_sum = max(max_sum,sum_attacked)
    return max_sum





t = int(input())
for _ in range(t):
    board = []
    maxVal = 0
    row,m = map(int,input().split())
    for _ in range(row):
        row = list(map(int,input().split()))
        maxVal = max(maxVal,max(row))
        board.append(row)
    print(xSum(board))