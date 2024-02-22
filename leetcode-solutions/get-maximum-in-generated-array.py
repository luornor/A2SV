class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        maxx = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[(i - 1) // 2] + dp[(i + 1) // 2]

            maxx = max(maxx, dp[i])

        return maxx

        


        
