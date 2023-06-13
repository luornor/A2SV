def twoSum(nums: list[int], target: int) -> list[int]:

    
    # brute force method
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]+nums[j]==target:
    #             return [i,j]
            
    #hash table method
    num_dict = {}
    for i in range(len(nums)):
        complement = target-nums[i]
        if complement in num_dict:
            return [num_dict[complement],i]
        else:
            num_dict[nums[i]]=i
            
    print(twoSum([2,7,11,15],9))