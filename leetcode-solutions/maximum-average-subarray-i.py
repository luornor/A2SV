class Solution:
    def findMaxAverage(nums, k: int):
        n = len(nums)
        #compute the first k average
        
        curr_sum = sum(nums[:k])
        max_avg = curr_sum/k
        r = 1
        while r<n-k+1:
            #to slide the window remove first element
            #and add next element
            curr_sum -= nums[r-1]
            curr_sum += nums[r+k-1]
            max_avg = max(max_avg,curr_sum/k)
            r+=1

        return max_avg
        