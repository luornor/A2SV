class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) 
        cost+=[0]   
        dp = [float('inf')]*(n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n+1):
            dp[i] = cost[i]+ min(dp[i-1],dp[i-2])


        # print(dp)
        return dp[-1]