def solve(n,b):
    l = 0
    r = n-1
    res = []
    if n==1:
        res.append(b[0])
    while l<r:
        res.append(b[l])
        l+=1
        res.append(b[r])
        r-=1
        if l==r:
            res.append(b[l])
        
    print(*res)



t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int,input().split()))
    solve(n,b)