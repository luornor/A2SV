
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    arr = []
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0 #represents the top most layers of the matrix
    bottom = rows-1 #represents the last row of the matrix
    right = cols-1 #represents the last column of the matrix
    left = 0 #represents the first column of the matrix
    if cols==1:
        for i in range(cols):
            for j in range(rows):
                arr.append(matrix[i][j])
    elif rows==1:
        for i in range(rows):
            for j in range(cols):
                arr.append(matrix[i][j])
    else:
        #move from left to right
        while top<=bottom and left<=right:
            i = left
            while i<=right:
                arr.append(matrix[top][i])
                i+=1
            top+=1
            #move from top to bottom
            i = top
            while i<=bottom:
                arr.append(matrix[i][right])
                i+=1
            right-=1
            
            if top>bottom or left>right: break
            #move from right to left reverse
            i = right
            while i>=left:
                arr.append(matrix[bottom][i])
                i-=1
            bottom-=1
            #move from bottom to top reverse
            i = bottom
            while i>=top:
                arr.append(matrix[i][left])
                i-=1
            left+=1
        
    return  arr

print(spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))