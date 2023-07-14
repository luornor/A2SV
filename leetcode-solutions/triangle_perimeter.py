"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths.
If it is impossible to form any triangle of a non-zero area, return 0.
"""
def largestPerimeter(nums: list[int]) -> int:
    nums.sort()
    dist = 0
    for i in range(len(nums)-2):
            if nums[i] + nums[i+1]>nums[i+2]:
                perim = nums[i+2] + nums[i+1] + nums[i]
                if perim>dist:
                    dist=perim
    return dist     
                       

print(largestPerimeter([1,2,1,10]))