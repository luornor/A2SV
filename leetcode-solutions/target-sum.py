class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dp(idx,currsum):
            
            if idx>=len(nums):
                if currsum==target:
                    return 1
                else:
                    return 0
            

            if (idx,currsum) not in memo:
                sub_1 = dp(idx+1,currsum+(1*nums[idx]))
                sub_2 =dp(idx+1,currsum+(-1*nums[idx]))
                
                memo[(idx,currsum)] = sub_1+sub_2
                    
            return memo[(idx,currsum)]


        return dp(0,0)

