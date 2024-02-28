class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def dp(l,r,turn):

            if l>r:
                return 0

            if (l,r,turn) not in memo:
                if turn:
                    memo[(l,r,turn)] = max(dp(l+1, r, False) + nums[l], dp(l,r-1,False)+nums[r])
                else:
                    memo[(l,r,turn)] = min(dp(l+1, r, True) - nums[l], dp(l,r-1,True)-nums[r])

            return memo[(l,r,turn)]
        
        n = len(nums)
        return dp(0,n-1,True)>= 0
        
        # dp = []