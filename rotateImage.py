"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""
def rotate(matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        #transpose the matrix 
        for row in range(rows):
            for col in range(row+1,cols):
                  matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
                  
        #then reverse each row
        for row in range(rows):
              matrix[row] = matrix[row][::-1]

        return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))