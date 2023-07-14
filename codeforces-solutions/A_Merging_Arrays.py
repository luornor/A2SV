n,m = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))


def solve(n,m,list1,list2):
    i = 0
    j = 0
    res = []
    while i<n and j<m:
        if list1[i]<=list2[j]:
            res.append(list1[i])
            i+=1
        
        else:
            res.append(list2[j])
            j+=1

    #append the remaining elements if any remains
    res.extend(list1[i:])
    res.extend(list2[j:])
    
    print(*res)


solve(n,m,list1,list2)


