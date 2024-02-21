class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(x,y):
            if x==m-1 or y==n-1:
                return 1

            if (x,y) not in memo:
                memo[(x,y)] = dp(x,y+1) + dp(x+1,y) 

            return memo[(x,y)]

        memo = {}
        return dp(0,0)


