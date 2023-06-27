def transpose(matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        new_mat = [[0] * rows for i in range(cols)]
        
        for col in range(cols):
            for row in range(rows):
                  new_mat[col][row]=matrix[row][col]
        return new_mat

                  
                   

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))