def countFairPairs(nums,lower,upper):
    count = 0
    nums.sort()
    n = len(nums)
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if i!=j:
    #             if lower<= nums[i]+nums[j]<=upper:
    #                 count+=1

    low = n-1
    high = n-1
    i = 0
    while i < high:
        low = max(i,low)
        while i<low and nums[i] + nums[low]>=lower:
            low-=1
        while low <high and nums[i]+nums[high]>upper:
            high-=1
        
        count+=high-low
        i+=1
    
    return count