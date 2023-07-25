def solve(n,a):
    
    min_val = min(a)
    min_index = a.index(min_val)
    # Check left side of the min value for increasing
    for l in range(min_index):
        if  a[l] < a[l+1]:
            return False

    # Check right side of the min value for increasing
    for r in range(min_index,n-1):
        if  a[r] > a[r+1]:
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

