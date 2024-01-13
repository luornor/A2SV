class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        res=[]
        while i<n:
            idx = nums[i]-1
            if nums[idx] != nums[i]:
                nums[idx],nums[i]=nums[i],nums[idx]
            else:
                i+=1

        for i in range(n):
            if nums[i] !=i+1:
                res.append(nums[i])

        return res