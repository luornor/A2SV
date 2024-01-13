class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            idx = nums[i]
            if idx != i and idx < n:
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1

        for i, num in enumerate(nums):
            if i != num:
                return i

        return n