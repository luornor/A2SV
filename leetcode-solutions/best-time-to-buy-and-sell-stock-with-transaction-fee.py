class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0]*2 for _ in range(len(prices)+1)]
        n = len(prices)
        dp[n][True] = 0
        dp[n][False] = 0

        for i in range(n-1,-1,-1):
            dp[i][True] = max(-prices[i]+dp[i+1][False],dp[i+1][True])
            dp[i][False] = max(prices[i]-fee+dp[i+1][True],dp[i+1][False])
        
        
        return dp[0][True]
        


    
            
