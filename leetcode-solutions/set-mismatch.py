class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            idx = nums[i]-1
            if nums[idx] != nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1

        res = []
        for i, num in enumerate(nums):
            if i+1 != num:
                res.append(num)
                res.append(i+1)

        return res
            
                 
        