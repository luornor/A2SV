def leftRightDifference(nums):
    
    n = len(nums)
    res = [0]*n
    for i in range(n):
        leftsum = 0
        rightsum = 0
        for j in range(0,i):
            leftsum+=nums[j]
        for k in range(i+1,n):
            rightsum+=nums[k]
        res[i]=abs(leftsum-rightsum)

    return res