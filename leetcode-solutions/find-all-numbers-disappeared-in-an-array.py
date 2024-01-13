class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        i = 0
        while i < n:
            idx = nums[i] - 1
            if nums[i] != nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1

        for i, num in enumerate(nums):
            if i + 1 != num:
                res.append(i + 1)

        return res
        