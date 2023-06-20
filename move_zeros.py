"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""

nums = [0,1,0,3,12]

for num in nums:
    if num==0:
        nums.append(nums.pop(nums.index(num)))
print(nums)

# Approach
# ● Set your read index accordingly to
# your need
# ● Set your write index accordingly to
# your need
# ● Your read should always move
# ● Your write only moves after write
# operation

# def moveZeroes(nums: list[int]):
#     write = 0
#     read = 0
#     while read < len(nums):
#         if nums[read] != 0:
#             #swap read with write
#             temp = nums[read]
#             nums[read] = nums[write]
#             nums[write] = temp
#             write = write + 1
#         read = read + 1
#     print(nums)

# moveZeroes(nums)    