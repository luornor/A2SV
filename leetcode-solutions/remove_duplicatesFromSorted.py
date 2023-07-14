class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        left = 1
        right = 1
        #1,1,2
        #0,0,1,1,1,2,2,3,3,4
        while right < n:
            if nums[right] == nums[left-1]:
                right+=1
            else:
                nums[left] = nums[right]
                left+=1
                right+=1
            
        return  left
        


