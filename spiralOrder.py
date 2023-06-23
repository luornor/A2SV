"""
To traverse a matrix in a spiral order, you can use a combination of loops and indices to control the movement in the desired pattern. Here's a step-by-step guide to traverse a matrix in a spiral order:

1. Define four variables: `top`, `bottom`, `left`, and `right`. These variables represent the boundaries of the current spiral layer in the matrix.
   - `top` represents the topmost row of the current layer.
   - `bottom` represents the bottommost row of the current layer.
   - `left` represents the leftmost column of the current layer.
   - `right` represents the rightmost column of the current layer.
   Initially, set `top = 0`, `bottom = number of rows - 1`, `left = 0`, and `right = number of columns - 1`.

2. Start a loop that continues while `top <= bottom` and `left <= right`. This condition ensures that there are still elements to traverse in the matrix.

3. Traverse the topmost row from left to right. Start a loop with an index variable `i` that goes from `left` to `right`. Access and process the element at `(top, i)`.

4. Increment `top` by 1 to exclude the topmost row from future traversal.

5. Traverse the rightmost column from top to bottom. Start a loop with an index variable `i` that goes from `top` to `bottom`. Access and process the element at `(i, right)`.

6. Decrement `right` by 1 to exclude the rightmost column from future traversal.

7. Check if there are still elements to traverse. If `top <= bottom` is false, break the loop.

8. Traverse the bottommost row from right to left. Start a loop with an index variable `i` that goes from `right` to `left` in reverse order. Access and process the element at `(bottom, i)`.

9. Decrement `bottom` by 1 to exclude the bottommost row from future traversal.

10. Traverse the leftmost column from bottom to top. Start a loop with an index variable `i` that goes from `bottom` to `top` in reverse order. Access and process the element at `(i, left)`.

11. Increment `left` by 1 to exclude the leftmost column from future traversal.

12. Repeat steps 7-11 until there are no more elements to traverse.

By following these steps, you can traverse a matrix in a spiral order, visiting each element exactly once.
"""
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
        while top<=bottom and left<=right:
            i = left
            while i<=right:
                arr.append(matrix[top][i])
                i+=1
            top+=1
            i = top
            while i<=bottom:
                arr.append(matrix[i][right])
                i+=1
            right-=1
            
            if top>bottom or left>right: break
            i = right
            while i>=left:
                arr.append(matrix[bottom][i])
                i-=1
            bottom-=1
            i = bottom
            while i>=top:
                arr.append(matrix[i][left])
                i-=1
            left+=1
        
    return  arr

print(spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))