class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        max_amount1 = dp[n - 2]

        dp = [0] * n
        dp[1] = nums[1]

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        max_amount2 = dp[n - 1]

        return max(max_amount1, max_amount2)