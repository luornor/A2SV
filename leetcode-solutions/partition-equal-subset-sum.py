class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        memo = {}
        def dp(idx,target):
            
            if idx>=len(nums) or target<=0:
                return target==0

            if (idx,target) not in memo:
                memo[(idx,target)]= dp(idx+1,target-nums[idx]) or dp(idx+1,target)

            return memo[(idx,target)]

        return sum(nums) %2==0 and dp(0,sum(nums)//2)


        