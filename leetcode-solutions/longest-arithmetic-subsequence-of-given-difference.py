class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        #what is the longest subsequence of the previous number
        #with the given difference
        dp = {}
        res = 1
        for num in arr:
            prev = dp.get(num-difference,0)
            dp[num] = prev+1
            res = max(res,dp[num])

        return res

            
        