class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom up
        dp=[float('inf')]*(amount+1)

        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i],1+dp[i-coin])
        # print(dp)

        if dp[-1]==float('inf'):
            return -1
        else:
            return dp[-1]

              