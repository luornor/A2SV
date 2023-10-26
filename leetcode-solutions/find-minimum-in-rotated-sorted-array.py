class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[m+1]:
                return nums[m+1]
            elif nums[m]<nums[m-1]:
                return nums[m]
            #if middle number is greater than last element
            #search search the right half
            elif nums[r]>nums[m]:
                r=m
            else:
                l=m
        return nums[l]
