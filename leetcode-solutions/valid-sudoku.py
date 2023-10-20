class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
        