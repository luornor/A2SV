class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n<=1:
                return n

            if n not in memo:
                if n%2==0:
                    memo[n] = dp(n//2)
                else:
                    memo[n] = dp((n-1)//2)+ dp((n+1)//2)

            return memo[n]

        maxx = 0
        for i in range(n+1):
            maxx = max(maxx, dp(i))

        return maxx

        


        
