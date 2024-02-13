class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==3:
            return 0
        l = 0
        r = len(nums)-4
        diff = float("inf")
        while r<len(nums) and l<len(nums):
            diff = min(diff,abs(nums[r]-nums[l]))
            l+=1
            r+=1


        # print(diff)
        if diff==float("inf"):
            return 0
        else:
            return diff

        