def matrixReshape(mat, r, c):
    rows = len(mat)
    cols = len(mat[0])
    new_mat = []

    if (rows*cols) == (r*c):
        arr = [mat[row][col] for row in range(rows) for col in range(cols)]
        idx = 0
        for i in range(r):
            new_arr = []
            for j in range(c):
                new_arr.append(arr[idx])
                idx+=1
            new_mat.append(new_arr)
        return new_mat               
    else:
        return mat


print(matrixReshape([[1,2],[3,4]],4,1))