def applyOperations(nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            else:
                continue
        for num in nums:
            if num==0:
                nums.append(nums.pop(nums.index(num)))
        return nums
print(applyOperations([1,0,2,0,0,1]))