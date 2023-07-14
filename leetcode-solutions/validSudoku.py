"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
import collections


def isValidSudoku(board: list[list[str]]) -> bool:
    sub_boxes = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    row_num = len(board)
    col_num = len(board[0])
    #Each row must contain the digits 1-9 without repetition.
    for row in range(row_num):
        for col in range(col_num):
            if board[row][col] != ".":
                if  (board[row][col] in rows[row] or
                      board[row][col] in cols[col] or 
                      board[row][col] in sub_boxes[(row//3,col//3)]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                sub_boxes[(row//3,col//3)].add(board[row][col])
    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))




    