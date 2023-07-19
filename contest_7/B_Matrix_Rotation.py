t = int(input())

def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    #transpose the matrix
    for r in range(rows):
        for c in range(r+1,cols):
            matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]

    #reverse each row
    for r in range(rows):
        matrix[r] = matrix[r][::-1]

    return matrix



def is_beautiful(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    #check if rows are in decreasing order
    for r in range(rows):
        if matrix[r][0]> matrix[r][1]:
            return False
            
    #check if columns are decreasing
    for c in range(cols):
        if matrix[0][c] > matrix[1][c]:
            return False
       
    return True
        
def check(row1,row2):
    matrix = [row1,row2]
    is_possible = False
    #because it's a 2 by 2 matrix
    for _ in range(4):
        if is_beautiful(matrix):
            is_possible=True
            break
        else:
            rotate(matrix)

    if is_possible:
        print('YES')
    else:
        print('NO')


for _ in range(t):
    row1 = list(map(int,input().split()))
    row2 = list(map(int,input().split()))

    check(row1,row2)

