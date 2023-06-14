"""Mihai has marked all squares the bishop attacks, but forgot where the bishop was! Help Mihai find the position of the bishop.

Input
The first line of the input contains a single integer t
 (1≤t≤36
) — the number of test cases. The description of test cases follows. There is an empty line before each test case.

Each test case consists of 8
 lines, each containing 8
 characters. Each of these characters is either '#' or '.', denoting a square under attack and a square not under attack, respectively.

Output
For each test case, output two integers r
 and c
 (2≤r,c≤7
) — the row and column of the bishop.

The input is generated in such a way that there is always exactly one possible location of the bishop that is not on the edge of the board."""
t = int(input()) #number of test cases

"""
.....#..
#...#...
.#.#....
..#.....
.#.#....
#...#...
.....#..
......#.
"""
def bishop(board):
    
    # for i in range(len(board)-1):
    #     for i in range(len(board)-1):
    #         if i==j and board[i][j]=='#' and board[i-1][j-1]=='#' and board[i+1][j+1]=='#' and board[i+1][j-1]=='#' and board[i-1][j+1]=='#':
    #             print(i+1,j+1)
    #         elif i>j and board[i][j]=='#' and board[i-1][j-1]=='#' and board[i+1][j+1]=='#' and board[i+1][j-1]=='#' and board[i-1][j+1]=='#':
    #             print(i+1,j+1)
    #         elif i<j and board[i][j]=='#' and board[i-1][j-1]=='#' and board[i+1][j+1]=='#' and board[i+1][j-1]=='#' and board[i-1][j+1]=='#':
    #             print(i+1,j+1)


    j =0
    for i in range (1,len(board)-1):
        j+=1
        if board[i][j]=='#' and board[i-1][j-1]=='#' and board[i+1][j+1]=='#' and board[i+1][j-1]=='#' and board[i-1][j+1]=='#':
            print(i+1,j+1)
            
        
           


for _ in range(t):
    input()
    board = []
    for row in range(8):
        row = input()
        board.append(row)
    bishop(board)

