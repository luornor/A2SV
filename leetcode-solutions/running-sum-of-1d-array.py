class Solution:
    def runningSum(nums):
        # running_sum = []
        currsum = 0
        n = len(nums)
        for i in range(n):
            currsum+=nums[i]
            nums[i]=currsum

        return nums