
def pancakeSort(arr):
    n = len(arr)
    res = []
    if sorted(arr)==arr:
        return res
    
    def flip(right):
        left = 0
        while left<right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
    
    
    #start from the end and focus on the largest number index
    for k in range(n-1,-1,-1):
        max_idx = k
        for j in range(k,-1,-1):
            #find max number index
            if arr[j]>arr[max_idx]: max_idx=j
        #flip the array up to the max index
        if k!=j:
            flip(max_idx)
            flip(k)
            res.append(max_idx+1)
            res.append(k+1)

    
        
        return res

print(pancakeSort([3,2,4,1]))