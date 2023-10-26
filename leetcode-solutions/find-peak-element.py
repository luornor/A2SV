class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l =0
        h=len(nums)-1
        #[1,2,3,1]
        # 0 1 2 3
        # l     h
        while l<h:
            m=(l+h)//2
            if nums[m]>nums[m+1]:
                h=m
            else:
                l=m+1
        return l
        