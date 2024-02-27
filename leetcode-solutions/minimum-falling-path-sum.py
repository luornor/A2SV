class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = matrix.copy()
        for r in range(rows-2,-1,-1):
            for c in range(cols):
                #directly below
                curr = dp[r+1][c]
                if c>0:
                    #left diagonal
                    curr = min(curr,dp[r+1][c-1])
                if c<rows-1:
                    #right diagonal
                    curr = min(curr,dp[r+1][c+1])
                dp[r][c] +=curr
                
        return min(dp[0])


        