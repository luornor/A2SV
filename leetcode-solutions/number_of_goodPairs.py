class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        pairs = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]==nums[j]:
                    pairs.append((i,j))
        return len(pairs)