"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

"""
def setZeroes(matrix: list[list[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        x = 1
        y = 1
        rows = len(matrix)
        cols = len(matrix[0])
        #check if a number in the first row is already zero(natural)
        for col in range(cols):
            if matrix[0][col]==0:x = 0

        #check if a number in the first column is already zero(natural)
        for row in range(rows):
            if matrix[row][0]==0: y = 0

        #mark elements in corresponding first row and first colomn as zero
        #when you find a zero in the inner matrix
        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[row][col]==0:
                    matrix[0][col]=0
                    matrix[row][0]=0
        
        #check if the marked row is zero
        # if it is set all elements in that row to zero
        for col in range(1,cols):
            if matrix[0][col]==0:
                #fixed row
                for row in range(rows):
                    matrix[row][col]=0
        
        #check if the marked column is zero
        # if it is set all elements in that column to zero 
        for row in range(1,rows):
            #fixed column
            if matrix[row][0]==0:
                for col in range(cols):
                    matrix[row][col]=0

        # check if there is any natural zero in the column
        if y==0:
            for row in range(rows):
                matrix[row][0]=0
        if x==0:
            for col in range(cols):
                matrix[0][col]=0
        return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))