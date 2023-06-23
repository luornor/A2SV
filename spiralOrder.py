def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
    arr = []
    for i in range(len(matrix)):
        if j % len(matrix)-1==0:
            i-=1
            arr.append(matrix[i][j])


        for j in range(len(matrix[0])):
            arr.append(matrix[i][j])
            if i%len(matrix)-1==0:
                j+=1
                arr.append(matrix[i][j])
    return arr