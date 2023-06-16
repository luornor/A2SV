
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row=0
    col=0
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    while row <num_rows:
        while col< num_cols:
            if target==matrix[row][col]:
                return True
            col+=1
        col=0
        row+=1