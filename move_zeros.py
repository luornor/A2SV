
nums = [0,1,0,3,12]

# for num in nums:
#     if num==0:
#         nums.append(nums.pop(nums.index(num)))
# print(nums)

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