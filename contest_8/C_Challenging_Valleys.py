def solve(n,a):
    # l, r = 0, n-1
    # valley = False
    # #3 2 2 1 2 2 3
    # while l <= r:
    #     if l==r and a[r]==a[l] and (l==0 or a[l]>a[l-1]) and (r==n-1 or a[r]<a[r+1]):
    #         valley = True
    #     l+=1
    #     r-=1
            
    # if valley:
    #     print('YES')
    # else:
    #     print('NO')
    min_val = min(a)
    l = a.index(min_val)
    # r = n - 1 - a[::-1].index(min_val)
    r = l+1


    # Check left side of the min value for decreasing
    for i in range(1,l+1):
        if  a[i] <= a[i-1]:
            return False

    # Check right side of the min value for increasing
    for i in range(r,n-1):
        if  a[i] >= a[i+1]:
            return False

    return True
            
        
      
    
    
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    res = solve(n,arr)
    if res==True:
        print('YES')
    else:
        print('NO')

