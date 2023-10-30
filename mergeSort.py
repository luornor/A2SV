
def merge(a,b):
    arr = []
    l = 0
    r = 0
    while l<len(a) and r<len(b):
        if a[l]<b[r]:
            arr.append(a[l])
            l+=1
        else:
            arr.append(b[r])
            r+=1

    while l<len(a):
        arr.append(a[l])
        l+=1
    
    while r<len(b):
        arr.append(b[r])
        r+=1

    return arr



def mergesort(arr):
    if len(arr)<=1:
        return arr
    
    m=len(arr)//2
    a = mergesort(arr[:m])
    b = mergesort(arr[m:])
    

    return merge(a,b)


print(mergesort([4,5,1,2,6,3]))