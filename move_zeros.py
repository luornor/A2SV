"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""

nums = [0,1,0,3,12]

for num in nums:
    if num==0:
        nums.append(nums.pop(nums.index(num)))
print(nums)

plc = 0 #placeholder pointer
seek = 0#seeker pointer
while seek< len(nums):
    if nums[seek]!=0:
        nums[plc],nums[seek] = nums[seek],nums[plc]
        plc+=1
        seek+=1
    else:
        seek+=1

# moveZeroes(nums)    