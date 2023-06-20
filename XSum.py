"""
Timur's grandfather gifted him a chessboard to practice his chess skills. 
This chessboard is a grid a with n rows and m
columns with each cell having a non-negative integer written on it.

Timur's challenge is to place a bishop on the board such 
that the sum of all cells attacked by the bishop is maximal. 
The bishop attacks in all directions diagonally, 
there is no limit to the distance which the bishop can attack. 
Note that the cell on which the bishop is placed is also considered attacked.
Help him find the maximal sum he can get.

Input
The first line of the input contains a single integer t
(1≤t≤100) — the number of test cases. The description of test cases follows.

The first line of each test case contains the integers n and m (1≤n≤200,1≤m≤200).
The following n lines contain m integers each, the j-th element of the i-th line aij
is the number written in the j-th cell of the i-th row (0≤aij≤106)
It is guaranteed that the sum of n⋅m over all test cases does not exceed 4⋅10^4.

Output
For each test case output a single integer, the maximum sum over all possible placements of the bishop.

"""
def xSum(board):
    max_sum = float('-inf')
    row = 0
    col = 0
    while row < len(board)-1 or col < len(board[0])-1:
        diagonal_sum = board[row][col] + board[row-1][col-1] + board[row+1][col+1]+ board[row+1][col-1]+ board[row-1][col+1]
        if diagonal_sum > max_sum:
            max_sum = diagonal_sum
        row+=1
        col+=1
                
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

