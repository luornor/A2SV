class Solution:
    def rotate(nums,k):
        """
        Do not return anything, modify nums in-place instead.
        """
        #make sure k does not exceed lenght of nums
        n = len(nums)
        k = k % n
        l = 0
        r = n-1
        # reverse the array
        while l<=r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        #reverse the first k elements
        l = 0
        r = k-1
        while l<=r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        #reverse the last n-k elements
        l = k
        r = n-1
        while l<=r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        
