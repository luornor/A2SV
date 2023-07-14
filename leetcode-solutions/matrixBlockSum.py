"""
Given a m x n matrix mat and an integer k,
return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix."""


def matrixBlockSum(mat, k):
    rows = len(mat)
    cols = len(mat[0])
    answer = [[0]*cols for _ in range(rows)]
   
    for i in range(rows):
        for j in range(cols):
            num = 0
            for r in range(max(0,i-k),min(rows,i+k+1)):
                for c in range(max(0,j-k),min(cols,j+k+1)):
                    num += mat[r][c]
            answer[i][j]=num
    return answer

print(matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],1))


