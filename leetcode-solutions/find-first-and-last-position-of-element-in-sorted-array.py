class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        res = []
        while l<=r:
            if nums[l]==target and nums[r]==target:
               return [l,r]
            elif nums[l]<target:
                l+=1
            elif nums[r]>target:
                r-=1
        return [-1,-1]
        