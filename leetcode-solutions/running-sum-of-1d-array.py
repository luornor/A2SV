class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        currsum = 0
        n = len(nums)
        for i in range(n):
            currsum+=nums[i]
            running_sum.append(currsum)

        return running_sum