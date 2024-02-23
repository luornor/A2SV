class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(n):

            if n>target:
                return 0
            if n==target:
                return 1
                
            if n not in memo:
                memo[n] = 0
                for num in nums:
                    if n<target:
                        memo[n] +=dp(n+num)

            return memo[n]

        return dp(0)
