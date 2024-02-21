class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)

        def dp(l,r):
            if l>r:
                return 0
            
            if (l,r) not in memo:
                memo[(l, r)] = max(dp(l+2,r)+nums[l],dp(l+1,r))

            return memo[(l, r)]
        
        n=len(nums)
        memo = {}
        return max(dp(0,n-2),dp(1,n-1))