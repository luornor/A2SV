class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            idx = nums[i]-1
            if nums[idx] != nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1

        for i, num in enumerate(nums):
            if i+1 != num:
                return num
        