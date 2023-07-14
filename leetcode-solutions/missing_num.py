class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing = 0
        for i in range(len(nums)+1):
            if i not in nums:
                missing = i

        return missing