class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dp(n):
            if n<0:
                return -1

            if n==0:
                return 0
            
            if n not in memo:
                memo[n] = float('inf')
                
                for coin in coins:
                    sub = dp(n-coin)
                    if sub>=0:
                        memo[n] = min(memo[n],sub+1)

            if memo[n]==float('inf'):
                return -1

            return memo[n]


        return dp(amount)