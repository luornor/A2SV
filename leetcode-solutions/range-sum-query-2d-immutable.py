class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.p_s = [[0]*(self.cols+1) for _ in range(self.rows+1)]
    
        for i in range(self.rows):
            for j in range(self.cols):
                self.p_s[i][j]=self.p_s[i-1][j]+self.p_s[i][j-1]-self.p_s[i-1][j-1]+self.matrix[i][j]
        # print(self.p_s)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.p_s[row2][col2]-self.p_s[row1-1][col2]-self.p_s[row2][col1-1]+self.p_s[row1-1][col1-1]
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)