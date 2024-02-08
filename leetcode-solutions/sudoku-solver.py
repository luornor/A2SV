class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board,num,r,c):
            #check if number is not in the row
            for i in range(9):
                if board[i][c]==num:
                    return False
            
            #check cols
            for j in range(9):
                if board[r][j]==num:
                    return False

            #check 3 by 3 grid
            row = 3*(r//3)
            col = 3*(c//3)
            for i in range(3):
                for j in range(3):
                    if board[i+row][j+col]==num:
                        return False

            return True


        def solve(board,r,c):
            #base cases

            if r == 9:  #reached the end of the board
                return True

            if c==9: #move to next row
                return solve(board,r+1,0)

            #if cell is filled already
            if board[r][c] != '.':
                return solve(board,r,c+1)

            #Try placing numbers 1-9
            for num in range(1,10): 
                #if number is valid assign to position
                if is_valid(board,str(num),r,c):
                    board[r][c]=str(num)

                    #if moving to next position yieds a solution
                    if solve(board,r,c+1):
                        return True
                    board[r][c]='.'

            return False

        solve(board,0,0)
    