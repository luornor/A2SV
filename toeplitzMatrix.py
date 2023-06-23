
def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    if rows==1 or cols==1:
        return True
    else:
        for i in range(rows-1):
            for j in range(cols-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
    return True

        


print(isToeplitzMatrix([[11,74,0,93],[40,11,74,7]]))