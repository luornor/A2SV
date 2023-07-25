class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        win_start = 0 #start of window
        min_size  = float('inf')  #minimum length of window
        running_sum = 0 #sum at each slide of the window
        for i in range(n):
            running_sum+=nums[i]

            while running_sum >=target:
                # if running_sum==target:
                min_size = min(min_size, i - win_start + 1)
                running_sum-=nums[win_start]
                win_start+=1
        
        if min_size != float('inf'):
            return min_size
        else:
            return 0

