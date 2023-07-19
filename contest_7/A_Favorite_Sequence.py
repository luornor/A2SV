t = int(input())

def solve(n,a):
    l = 0
    r = n-1
    res = []
    if n==1:
        res.append(a[0])
    while l<r:
        res.append(a[l])
        l+=1
        res.append(a[r])
        r-=1
        if l==r:
            res.append(a[l])
    print(*res)
        
    
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)
